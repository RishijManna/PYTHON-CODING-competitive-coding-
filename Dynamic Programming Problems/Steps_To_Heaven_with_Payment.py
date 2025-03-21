#in this given problem,person can step 1/2/3 steps at a time.
'''
🪜 Problem Statement: Minimum Cost to Climb Stairs
  A person wants to climb to the top of a staircase with n steps. They can take 1, 2, or 3 steps at a time. However, there is a fee associated with standing on each step. The goal is to find the minimum cost to reach the top.

Goal:
  Calculate the minimum fee required to reach step n by choosing the optimal steps.

Input:
  An integer n representing the number of steps.
  A list of integers where fees[i] is the cost to stand on step i+1.
  Output:
  An integer representing the minimum fee required to reach step n.
Constraints:
  To reach step i, you can:
  Come from step i-1 and pay fees[i-1].
  Come from step i-2 and pay fees[i-2].
  Come from step i-3 and pay fees[i-3].
'''

def stair_to_hev_pay(n,fees):
  min_fee=[0]*(n+1)  # min_fee[0] = 0 e hobe kano ki 0te pouchate kono taka lagbe na but 0te darate only taka lage.
  min_fee[1]=fees[0] # min_fee[1] = fees[0] hobe kano ki 1step e pouchate hole 0 te darate joto taka lage seta e lagbe sudhu. Mane direct 0 thake 1 jump
  min_fee[2]=fees[0] # min_fee[2] = fees[0] hobe kano ki 2step e pouchate hole 0 te darate joto taka lage seta e lagbe sudhu,kano ki step 1 er extra charges hobe na.
  #0 thake 2 e direct jump korlam
  print("min_fee",min_fee)
  for i in range(3,n+1):
    #aita mane ith step e pouchate min koto ta costing
    min_fee[i]=min(min_fee[i-1]+fees[i-1],min_fee[i-2]+fees[i-2],min_fee[i-3]+fees[i-3])
    #ai khane ager je step ta ke nebo setar daranor cost(fee[i-..])+ oto dur asar jonne ja cost(min_fee[i-....]). last 3step e jeta min possible setae store hobe.
  print("min_fee",min_fee)
  return min_fee[n]

n=int(input("Enter the number of steps that has to be climbed: "))
fees=list(map(int,input("Enter the fees for each step: ").split()))
print("fee",fees)
print(stair_to_hev_pay(n,fees))
