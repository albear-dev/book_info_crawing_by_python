import logging

class CRLogger:

    @classmethod
    def get_logger(cls, name):
        """로거 인스턴스 반환
        """

        __logger = logging.getLogger(name)

        # 로그 포멧 정의
        #formatter = logging.Formatter('BATCH##AWSBATCH##%(levelname)s##%(asctime)s##%(message)s >> @@file::%(filename)s@@line::%(lineno)s')
        formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(threadName)s][%(filename)s][line::%(lineno)s] %(message)s')
        # 스트림 핸들러 정의
        stream_handler = logging.StreamHandler()
        # 각 핸들러에 포멧 지정
        stream_handler.setFormatter(formatter)
        # 로거 인스턴스에 핸들러 삽입
        __logger.addHandler(stream_handler)
        # 로그 레벨 정의
        __logger.setLevel(logging.DEBUG)

        return __logger