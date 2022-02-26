from collections import Counter

total_test_cases = int(input())
max_tweet_id = {}
tweet_case_count = 0

for case in range(total_test_cases):
	total_tweets = int(input())
	tweets = []

	for tweet in range(total_tweets):
		tweet_input = str(input())
		tweets.append(tweet_input)
	
	username = [name.split()[0] for name in tweets]

	frequent_user = Counter(username)
	frequent_user_values = frequent_user.values()

	
	for (key, value) in sorted(frequent_user.items()):
		if value == max(frequent_user_values):
			max_tweet_id[tweet_case_count] = {key:value}
			tweet_case_count+=1

for (max_key, max_value) in max_tweet_id.items():
	for (key, value) in max_tweet_id[max_key].items():
		print(key + " " + str(value))