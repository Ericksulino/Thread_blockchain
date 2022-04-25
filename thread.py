import threading
import time
import subprocess
N = 10
T = 60
#cmd = 'docker exec cli peer chaincode invoke -o orderer.example.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n emr_contract --peerAddresses peer0.org1.example.com:7051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses peer0.org2.example.com:9051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{"Args":["issue","Pedro","accessinfo","123"]}'
def funcao():
    for i in range(N):
        #sreturn_code = subprocess.call("echo Hello World", shell=True)
        return_code = subprocess.run("exit 1", shell=True)

        


print("Inicio")
for i in range(T):
    print(i)
    threading.Thread(target=funcao).start()
    time.sleep(1)
print(return_code)
print("Fim")