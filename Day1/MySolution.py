a = [10,15,3,7]
k=17

# Using two pass 
def two_pass(a,k):
    count=0
    for i in range(len(a)):
        for j in range(len(a)):
            sum1=0
            sum1+=a[i]+a[j]
            if(sum1==k):
                count+=1
    if(count!=0):
        return True
    else:
        return False

# Using one pass 
def one_pass(a,k):
    i=0
    j=0
    count=0
    while(i<len(a)):
        if(j<len(a)):
            sum1=0
            sum1+=a[i]+a[j]
            if(sum1==k):
                count+=1
            j+=1
        else:
            i+=1
            j=0
    if(count!=0):
        return True
    else:
        return False
            
# Two pass Result   
ans=two_pass(a,k)
if(ans):
    print("List numbers are add upto K")
else:
    print("List numbers are not add upto K") 
# One pass Result
ans1=one_pass(a,k)
if(ans1):
    print("List numbers are add upto K")
else:
    print("List numbers are not add upto K") 
