from mac.csma import CSMA_MAC 
from mac.base import simulation 
import numpy as np 
from utils import MyLogger

logger = MyLogger() 

# CSMA_MAC 클래스를 상속하여 여러인자를 받아 초기화
class CSMA_CD_MAC(CSMA_MAC):
    def __init__(self, env, node, *args, **kwargs):
        super().__init__(env, node, *args, **kwargs)

        # backoff 변수는 충돌이 발생했을 대 동작을 수행하기 위한 플래그로 사용
        self.backoff = False 

    @simulation
    # 충돌이 감지되었을때 호출되는 함수
    def on_collision_detected(self, link, packet):
        # 전송이 진행중인지 확인
        if self.is_transmitting:
            # 전송 중이라면, stop_transmit 메서드 호출하여 전송 중지
            yield self.env.process(self.node.stop_transmit())

            # send_jamming_signal 메서드를 호출하여 충돌 감지 신호 전송
            self.node.send_jamming_signal()
            # 백오프 동작 활성화
            self.backoff = True

            # 여기 이후에 전송 오류로 처리가 되어서 아래의 on_transmission_failed 함수 실행됨


    @simulation
    # 충돌 감지 신호를 수신한 경우 호출되는 함수
    def on_receive_jamming_signal(self):
        # 메서드 호출하여 전송 중지
        yield self.env.process(self.node.stop_transmit())
        self.backoff = True

    @simulation 
    # 전송이 실패한 경우 호출되는 함수
    def on_transmission_failed(self, link, packet, reason):
        if self.backoff:
            # 백오프 슬롯의 수를 랜덤하게 선택하여 대기한 다음 transmit_packet 함수를 호출하여 패킷 재전송
            num_slots = np.random.randint(0, 2 **self.tx_attempt)
            yield self.env.timeout(link.SLOT_TIME * num_slots)

        yield self.env.process(self.transmit_packet(link,packet))

    @simulation 
    # 백오프 상태 해제 함수
    def on_transmission_success(self, link, packet):
        self.backoff - False

    #보내면서 확인 