import time

class UserRateLimiter:
    def __init__(self, capacity, refill_rate, refill_interval):
        """
        Initialize the rate limiter with the given capacity, refill rate, and refill interval.

        :param capacity: Maximum number of tokens the bucket can hold.
        :param refill_rate: Number of tokens to be added to the bucket per refill_interval.
        :param refill_interval: Time interval (in seconds) at which the tokens are added to the bucket.
        """
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.refill_interval = refill_interval
        self.last_refill_time = time.time()

    def refill(self):
        """
        Refill the bucket with tokens based on the refill_rate and refill_interval.
        """
        current_time = time.time()
        time_since_last_refill = current_time - self.last_refill_time
        tokens_to_add = int(time_since_last_refill / self.refill_interval) * self.refill_rate

        if tokens_to_add > 0:
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_refill_time = current_time
            print(f"Refilled: tokens_to_add={tokens_to_add}, current_time={current_time}, last_refill_time={self.last_refill_time}, tokens={self.tokens}")
        else:
            print("Not refilled")



    def consume(self, tokens):
        """
        Consume the specified number of tokens from the bucket.

        :param tokens: Number of tokens to consume.
        :return: True if tokens are available and consumed, False otherwise.
        """
        
        self.refill()

        if tokens <= self.tokens:
            self.tokens -= tokens
            print("tokens in bucket", self.tokens)
            return True
        else:
            print("false tokens in bucket", self.tokens)
            return False


class RateLimiter:
    def __init__(self, user_capacity, user_refill_rate, user_refill_interval):
        """
        Initialize the rate limiter with user-specific parameters.

        :param user_capacity: Maximum number of tokens a user's bucket can hold.
        :param user_refill_rate: Number of tokens to be added to a user's bucket per user_refill_interval.
        :param user_refill_interval: Time interval (in seconds) at which the tokens are added to a user's bucket.
        """
        self.user_rate_limiters = {}
        self.user_capacity = user_capacity
        self.user_refill_rate = user_refill_rate
        self.user_refill_interval = user_refill_interval

    def get_user_limiter(self, user_identifier):
        """
        Get or create a rate limiter for the specified user.

        :param user_identifier: Identifier for the user (e.g., user ID, IP address, etc.).
        :return: UserRateLimiter instance for the specified user.
        """
        if user_identifier not in self.user_rate_limiters:
            # Create a new UserRateLimiter instance only if it doesn't exist
            self.user_rate_limiters[user_identifier] = UserRateLimiter(
                self.user_capacity, self.user_refill_rate, self.user_refill_interval
            )
        return self.user_rate_limiters[user_identifier]

    def consume(self, user_identifier, tokens=1):
        """
        Consume the specified number of tokens from the user's bucket.

        :param user_identifier: Identifier for the user.
        :param tokens: Number of tokens to consume.
        :return: True if tokens are available and consumed, False otherwise.
        """
        user_limiter = self.get_user_limiter(user_identifier)
        return user_limiter.consume(tokens)

# Example usage:
limiter = RateLimiter(user_capacity=10, user_refill_rate=1, user_refill_interval=60)

# Simulate requests from different users or IP addresses
# identifiers = ["user1", "user2", "192.168.0.1"]
# for identifier in identifiers:
#     for i in range(15):
#         if limiter.consume(identifier):
#             print(f"Identifier {identifier}, Request {i + 1}: Accepted")
#         else:
#             print(f"Identifier {identifier}, Request {i + 1}: Rejected (Rate Limit Exceeded)")
#         time.sleep(0.2)  # Simulate some delay between requests

identifier = "user1"
for i in range(15):
    if limiter.consume(identifier):
        print(f"Identifier {identifier}, Request {i + 1}: Accepted")
    else:
        print(f"Identifier {identifier}, Request {i + 1}: Rejected (Rate Limit Exceeded)")
    time.sleep(0.4)  # Simulate some de

time.sleep(0.1)
print("***************")
for i in range(8):
    if limiter.consume(identifier):
        print(f"Identifier {identifier}, Request {i + 1}: Accepted")
    else:
        print(f"Identifier {identifier}, Request {i + 1}: Rejected (Rate Limit Exceeded)")
    time.sleep(0.5)  # Simulate some de

