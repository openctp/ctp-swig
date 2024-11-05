"""
@Author: Jedore(https://github.com/Jedore)
@Date: 04/11/2024
"""

from queue import Queue

Q_CONNECT = Queue(maxsize=1)
Q_LOGIN = Queue(maxsize=1)

TIMEOUT = 5  # seconds

import thostmduserapi as api


class CMdSpiImpl(api.CThostFtdcMdSpi):
    def __init__(self, md_api):
        super().__init__()
        self.md_api = md_api

    def OnFrontConnected(self):
        Q_CONNECT.put(True, timeout=TIMEOUT)
        req = api.CThostFtdcReqUserLoginField()
        self.md_api.ReqUserLogin(req, 0)

    def OnRspUserLogin(self, pRspUserLogin: api.CThostFtdcRspUserLoginField,
                       pRspInfo: api.CThostFtdcRspInfoField, nRequestID: int,
                       bIsLast: bool):
        if pRspInfo is None or pRspInfo.ErrorID == 0:
            # success
            Q_LOGIN.put(True, timeout=TIMEOUT)
        else:
            # failed
            Q_LOGIN.put(False, timeout=TIMEOUT)


def test_mdapi():
    # Success if at least 1 md front success.
    md_fronts = (
        'tcp://180.168.146.187:10131',
        'tcp://180.168.146.187:10211',
        'tcp://180.168.146.187:10212',
        'tcp://180.168.146.187:10213',
    )
    error = None
    for md_front in md_fronts:
        try:
            mdapi = api.CThostFtdcMdApi.CreateFtdcMdApi()
            mdspi = CMdSpiImpl(mdapi)
            mdapi.RegisterFront(md_front)
            mdapi.RegisterSpi(mdspi)
            mdapi.Init()

            try:
                Q_CONNECT.get(timeout=TIMEOUT)
            except:
                print('Test Failed: mdapi')
                assert False, 'Connect Failed!'

            try:
                if not Q_LOGIN.get(timeout=TIMEOUT):
                    print('Test Failed: mdapi')
                    assert False, 'Login Failed!'

            except:
                print('Test Failed: mdapi')
                assert False, 'Login Failed!'

            # success
            print('Test Succeed: mdapi')
            break
        except AssertionError as e:
            error = str(e)
    else:
        # Failed
        print('Test Failed: mdapi')
        assert False, error


if __name__ == '__main__':
    test_mdapi()
