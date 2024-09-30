class Solution:

	def matchPairs(self, n, nuts, bolts):
		# code here
		# Define the order of the elements
        order = ['!', '#', '$', '%', '&', '*', '?', '@', '^']
        
        # Create a dictionary for quick lookup of order
        order_dict = {char: i for i, char in enumerate(order)}
        
        # Sort both nuts and bolts according to the order dictionary
        nuts.sort(key=lambda nut: order_dict[nut])
        bolts.sort(key=lambda bolt: order_dict[bolt])
