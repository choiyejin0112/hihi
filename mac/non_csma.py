from mac.base import BaseMAC, simulation
from utils import MyLogger


logger = MyLogger() 


# BaseMAC 클래스를 상속하여 여러 인자를 받아 초기화
class NonCSMA_MAC(BaseMAC):
    def __init__(self, env, node, *args, **kwargs):
        super().__init__(env, node, *args, **kwargs)

    @simulation
    # link와 packet을 전달 받아 데이터 패킷을 전송함
    def transmit_packet(self, link, packet):
        # 변수를 증가시키고
        self.tx_attempt +=1
        # tx_attempt가 RETRANSMIT_LIMIT보다 크면
        if self.tx_attempt > self.RETRANSMIT_LIMIT:
            # yield = return이라 생각하셈
            # 재전송을 멈춤(중지)
            yield self.env.timeout(0.0)
        # 아니면
        else:
            #transmit 메서드 실행 -> 재전송한다
            yield self.env.process(self.node.transmit(link,packet))


    @simulation 
    # 전송이 실패한 경우 호출됨 / 실패한 이유 전달받음
    def on_transmission_failed(self, link, packet, reason):
        #실패하면 다시 보내셈 transmit_packet으로
        yield self.env.process(self.transmit_packet(link,packet))

        #무식하게 보내는 mac에서 노드수를 줄인다 -> 네트워크 간단하게 함(단순하게)/ 혼잡방지