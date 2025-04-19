class Process:
  def __init__(self,pid,processes):
    self.pid=pid
    self.alive=True
    self.processes=processes
    self.coordinator=None


  def start_election(self):
    print(f"\nProcess {self.pid} initiaes the election")

    higher=[p for p in self.processes if p.pid>self.pid and p.alive]

    if not higher:
      self.become_coordinator()
    else:
      for p in higher:
        print(f"Process {self.pid} sends election message to {p.pid}")
      for p in higher:
        p.respond_to_election(self)

  def respond_to_election(self,initiator):
    print(f"Process {self.pid} (alive) responds to elec tion message from {initiator.pid}")
    self.start_election()

  def become_coordinator(self):
    self.coordinator=self.pid
    print(f"\nProcess {self.pid} becomes the coordinator")
    for p in self.processes:
      if p.alive and p.pid != self.pid:
        p.coordinator=self.pid
        print(f"Process {self.pid} infroms process {p.pid} that it is the new coordinator")

processes=[Process(pid,[]) for pid in [1,2,3,4,5]]

for p in processes:
  p.processes=processes

processes[4].alive=False

processes[1].start_election()
