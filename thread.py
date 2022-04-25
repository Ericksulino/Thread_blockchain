import threading
import time
import subprocess
import timeit

N = 10
T = 10
#cmd = 'docker exec cli peer chaincode invoke -o orderer.example.com:7050 --tls true --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n emr_contract --peerAddresses peer0.org1.example.com:7051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses peer0.org2.example.com:9051 --tlsRootCertFiles /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{"Args":["issue","Pedro","accessinfo","123"]}'
def funcao():
    for i in range(N):
        inicio = timeit.default_timer()
        #sreturn_code = subprocess.call("echo Hello World", shell=True)
        return_code = subprocess.call("exit 1", shell=True)
        fim = timeit.default_timer()
        print(i,"return code: ",return_code,'duracao: %f' % (fim - inicio))
        


print("Inicio")

for i in range(T):
    print("execução: ",i)
    threading.Thread(target=funcao).start()
    time.sleep(1)

print("Fim")