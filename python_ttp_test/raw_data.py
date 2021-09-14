ospf_raw1 = '''
#--------------------------------------------------
echo "OSPFv2 Configuration"
#--------------------------------------------------
        ospf 0
            asbr
            traffic-engineering
            area 0.0.0.0
                interface "system"
                    shutdown
            area 0.0.0.60
                interface "system"
                    no shutdown
                exit
                interface "to-me-d6-bog"
                    interface-type point-to-point
                    authentication-type message-digest
                    message-digest-key 1 md5 "5ySJ9bHyyYfOe/JeANt2/74FMFriyuoUiuEA0kVckPfWxZ/X1e3GG/xeTieLB3S3" hash2
                    no shutdown
                exit
                interface "to-me-d6-lpk"
                    interface-type point-to-point
                    authentication-type message-digest
                    message-digest-key 1 md5 "5ySJ9bHyyYfOe/JeANt2/74FMFriyuoU4GkTI1RO0pEDt.z/t1gDh36/vJVeMU33" hash2
                    no shutdown
                exit
                interface "to-me9-d6-smd"
                    interface-type point-to-point
                    authentication-type message-digest
                    message-digest-key 1 md5 "jFKs4SSFkp7WSmBtHvwcHTyijn7In1dPvZ9QxgOPVJEdKRzXvzI0PjONBzNr1Xew" hash2
                    no shutdown
                exit
                interface "to-me-d6-mbd"
                    interface-type point-to-point
                    metric 65000
                    authentication-type message-digest
                    message-digest-key 1 md5 "5ySJ9bHyyYfOe/JeANt2/74FMFriyuoUI2AMlF61x9L/SlE3kGhICbNdNUrVMQQt" hash2
                    no shutdown
                exit
            exit
        exit
        '''

ospf_raw2 = '''
#--------------------------------------------------
echo "OSPFv2 Configuration"
#--------------------------------------------------
        ospf 0
            asbr
            traffic-engineering
            export "static-to-ospf"
            area 0.0.0.60
                interface "system"
                    no shutdown
                exit
                interface "to-me-d6-sgt"
                    interface-type point-to-point
                    authentication-type message-digest
                    message-digest-key 1 md5 "5ySJ9bHyyYfOe/JeANt2/74FMFriyuoURQLXfVJ67qjukXrttYGEBoKft1EJDUJS" hash2
                    no shutdown
                exit
                interface "to-me-d6-tsn"
                    interface-type point-to-point
                    authentication-type message-digest
                    message-digest-key 1 md5 "5ySJ9bHyyYfOe/JeANt2/74FMFriyuoUFmnA3qFuhpSbQpVsUd5NaXpyZ4ihkiNN" hash2
                    no shutdown
                exit
                interface "to-me9-d6-smd"
                    interface-type point-to-point
                    authentication-type message-digest
                    message-digest-key 1 md5 "jFKs4SSFkp7WSmBtHvwcHTyijn7In1dPvZ9QxgOPVJEdKRzXvzI0PjONBzNr1Xew" hash2
                    no shutdown
                exit
            exit
            no shutdown
        exit
        '''
