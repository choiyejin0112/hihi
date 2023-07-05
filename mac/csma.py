from mac.non_csma import NonCSMA_MAC
from mac.base import simulation 
from utils import MyLogger

logger = MyLogger() 


# NonCSMA_MAC 클래스를 상속하여 여러 인자를 받아 초기화
class CSMA_MAC(NonCSMA_MAC):
    def __init__(self, env, node, *args, **kwargs):
        super().__init__(env, node, *args, **kwargs)

    @simulation
    # 객체의 wait_until_idle 메서드를 호출하여 링크가 사용 가능한지 확인
    def transmit_packet(self, link, packet):
        #보내기 전에 확인하는 코드
        yield self.env.process(self.node.wait_until_idle())

        self.tx_attempt +=1
        # tx_attempt가 RETRANSMIT_LIMIT보다 크면
        if self.tx_attempt > self.RETRANSMIT_LIMIT:
            # 재전송을 멈춤(중지)
            yield self.env.timeout(0.0)
        else:
            #transmit 메서드 실행 -> 재전송한다
            yield self.env.process(self.node.transmit(link,packet))

# 먼저 노드 잡은사람이 임자 / no_csma보다 전달률 굳!