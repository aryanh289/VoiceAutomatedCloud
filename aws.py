import os 
import speech_recognition as sr
import time

r = sr.Recognizer()

def cap():
    print('CAPABILITES:')
    print('0. Connect to AWS')
    print('1. Launch an Instance')
    print('2. Start an Instance')
    print('3. Stop an Instance')
    print('4. Terminate an Instance')
    print('5. List the Instances')
    print('6. Create a volume')
    print('7. Attach the volume')
    print('8. Delete a volume')
    print('9. Detach the volume')
    print('10. Clear the terminal')

a = 1

while a:
    with sr.Microphone() as source:
        os.system("say 'Command'")
        print('command:')
        input()
        audio = r.listen(source)
        text = r.recognize_google(audio).lower()
        
        print(text)
        if(text=='show me your capabilities' or text=='show me what can you do?' or text=='what can you do?'):
            os.system("say 'Capable of following:'")
            cap()
            
        elif(text=='connect to cloud'):
            print('connecting')
            os.system("say 'connecting...'")
            os.system('aws configure')
            os.system("say 'Input Access ID and Key'")
            #os.system('AKIA4******************') //aws login creds
            #os.system('93z6R4hWaRpq*******************')
            os.system("say 'connected!'")
            os.system('aws ec2 describe-instances')
            os.system("say 'task completed'")
            
        elif(text=='start an instance'):
            os.system("say 'starting...'")
            os.system('aws ec2 start-instances --instance-id i-045689ba6077e3d37')
            #os.system('i-045689ba6077e3d37')
            os.system("say 'started!'")
            os.system('aws ec2 describe-instances')
            os.system("say 'task completed'")  
        
        elif(text=='stop an instance'):
            os.system("say 'stopping...'")
            os.system('aws ec2 stop-instances --instance-id i-045689ba6077e3d37')
            #os.system('i-045689ba6077e3d37')
            os.system("say 'stopped!'")
            os.system('aws ec2 describe-instances')
            os.system("say 'task completed'")  
            
        elif(text=='launch an instance'):
            os.system("say 'Launch process begins...'")
            os.system('aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --count 1 --security-group-ids sg-57449030 --key-name harshu99')
            time.sleep(5)
            os.system("say 'launched an instance !'")
            os.system('aws ec2 describe-instances')
            os.system("say 'task completed'")  
            
        elif(text=='terminate an instance'):
            os.system("say 'stopping...'")
            os.system('aws ec2 terminate-instances --instance-id i-0a9274f616d392e0e')
            os.system("say 'stopped!'")
            os.system('aws ec2 describe-instances')
            os.system("say 'task completed'") 
            
        elif(text=='list the instances'):
            os.system('aws ec2 describe-instances')
            os.system("say 'task completed'") 
            
        elif(text=='create a volume'):
            os.system("say 'creating a single volume of 1GB...'")
            os.system('aws ec2 create-volume --availability-zone ap-south-1a --size 1')
            os.system("say 'volume created'") 
            os.system("say 'task completed'") 
            
        elif(text=='attach the volume with the instance'):
            os.system("say 'attaching...'")
            os.system('aws ec2 attach-volume --volume-id vol-0a4c8f5f3502abc1f --instance-id  i-049ad3710a8955300 --device /dev/sdf')                        
            os.system("say 'attached!'")
            os.system("say 'task completed'") 
            
        elif(text=='detach the volume'):
            os.system("say 'detaching...'")
            os.system('aws ec2 detach-volume --volume-id vol-024d9f9ec9f6f4430 --instance-id i-045689ba6077e3d37 --device /dev/sdf')                         
            os.system("say 'detached!'")
            os.system("say 'task completed'") 
            
        elif(text=='delete the volume'):
            os.system("say 'deleting the volume...'")
            os.system('aws ec2 delete-volume --volume-id vol-024d9f9ec9f6f4430')
            os.system("say 'volume deleted'")
            os.system("say 'task completed'") 
    
        elif(text=='clear the terminal'):
            os.system("say 'clearing the terminal'")
            os.system('clear') 
                        
        elif(text=='bye bye'):
            os.system("say 'Have a good day sir!'")
            print('Have a good day sir!')
            a = 0
        else:    
            print("Thanks for commanding Master Harsh")
            os.system("say 'Thanks for commanding Master Harsh'")   

                    
        

    
            
        
    
    
