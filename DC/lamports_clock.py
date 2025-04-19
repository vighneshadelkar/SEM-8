# lamports logical clock

clock_1=0
clock_2=0

def send(clock):
  clock+=1
  return clock

def receive(receiver_clock,sender_clock):
  return max(receiver_clock,sender_clock)+1

communiation_queue=[]

while True:
  print("\n--- Menu ---")
  print("1. Process 1 sends packet")
  print("2. Process 2 sends packet")
  print("3. Process 1 receives packet")
  print("4. Process 2 receives packet")
  print("5. Exit")
  choice=int(input("Enter your choice: "))

  if choice== 1:
    clock_1=send(clock_1)
    communiation_queue.append((clock_1,'P1'))
    print(f"Process 1 sends packet with clock {clock_1}")
  elif choice==2:
    clock_2=send(clock_2)
    communiation_queue.append((clock_2,'P2'))
    print(f"Process 2 sends packet with clock {clock_2}")
  elif choice==3:
    if communiation_queue:
      packet=communiation_queue.pop(0)
      clock_1=receive(clock_1,packet[0])
      print(f"Process 1 receives packet from {packet[1]} with clock {packet[0]}. Updated clock: {clock_1}")
    else:
      print("No packets to receive.")
  elif choice==4:
    if communiation_queue:
      packet=communiation_queue.pop(0)
      clock_2=receive(clock_2,packet[0])
      print(f"Process 2 receives packet from {packet[1]} with clock {packet[0]}. Updated clock: {clock_2}")
    else:
      print("No packets to receive.")
  elif choice==5:
    break
  else:
    print("Invalid choice. Please try again.")

  print("\nFinal clocks:")
  print(f"Process 1: {clock_1}")
  print(f"Process 2: {clock_2}")
