# berkeley algorithm

def berkeley_algo(master_time,client_times):
  print(f"master time: {master_time}")
  print(f"client times: {client_times}")

  diffs=[client_time-master_time for client_time in client_times]
  print(f"time differences: {diffs}")

  avg_time=sum(diffs)/(len(client_times)+1)
  print(f"avg differences: {avg_time}")

  new_master_time=master_time+avg_time
  print(f"new master time: {new_master_time}")
  adjustments = []
  for i, client_time in enumerate(client_times):
    adjustment = new_master_time - client_time
    adjustments.append(adjustment)
    print(f"Client {i} should adjust by {adjustment:.2f}")

  return new_master_time,adjustments

master_time= 10.0
client_times=[12.0,8.0,11.5]

berkeley_algo(master_time,client_times)
