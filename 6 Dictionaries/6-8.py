l1={
    'pet':'abc',
    'owner':'xyz'
}
l2={
    'pet':'def',
    'owner':'pqr'
}
l3={
    'pet':'ghi',
    'owner':'stu'
}

pets=[l1,l2,l3]
for l in pets:
    print(f"owner:{l['pet']}")
    print(f"pet:{l['owner']}")