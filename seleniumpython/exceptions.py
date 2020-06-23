try:
    4/0
    print('no fail')

except Exception as e:
    print(e)

finally:
    print("finallly block")