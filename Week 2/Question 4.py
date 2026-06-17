def find_common_users(list1, list2):
    # Convert the first list to a set, then intersect with the second list
    return list(set(list1).intersection(list2))

# Example 1: Alphanumeric User IDs 
marketing_campaign_clicks = ['usr_85453', 'usr_92110', 'usr_33412', 'usr_77651']
completed_checkout = ['usr_33412', 'usr_55490', 'usr_85453', 'usr_11209']

common_alpha = find_common_users(marketing_campaign_clicks, completed_checkout)
print("Common Users (Alphanumeric IDs):", common_alpha)
# Output: ['usr_85453', 'usr_33412']