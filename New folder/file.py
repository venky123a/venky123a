#problem 1:
#Given an array of integers nums and integer target, return indices of the two numbers such that they add up to target. 
#you may assume that each input would have exactly one solution, and you may not use the same element twice.
#you can return the answer in any order.

#example 1:
input:nums=[2,7,11,15], target=9
output;[0,1]
#explanation:nums[0]+nums[1]=2+7=9,so the indices of the two numbers are[0,1]

#example 2:
input:nums=[3,1,5,8], 
target=6
output:[1,2]
#explanation:nums[1]+nums[2]=1+5=6,so the indices of the two n8umbers are [1,2]

#problem 2:
#given a strings containing characters'(',')','{','}','['and']' determine if the string is vaild
#an input string is vaild is:
#open brackets must be closed by the same type of brackets.
#open brackets must be closed in the correct order.
#every close bracket has a corresponding open bracket of the same type.

#Example 1:
input: s="[(]T."
output: False 

#Example 2:
input: s= "(([]))C.T."
output: False

#Problem 3:
#Given an integer array nums and an integer k, return the k most frequent elements. you may return the answer in any order.

#Example 1:
input: nums=[1,1,1,2,2,3], k=2
output: [1,2]

#Example 2:
input: nums=[3,1,4,4,5,2,6,1],k=3
output: [1,4,2]        

          