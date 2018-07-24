class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        say = '1'
        for r in range(n-1):
            count = 0
            buff = [say[0]]
            count_buff = []
            for index in range(len(say)):
                if say[index] == buff[-1]:
                    count += 1
                elif say[index] != buff[-1]:
                    count_buff.append(count)
                    count = 1
                    buff.append(say[index])
                if index == len(say) - 1:
                    count_buff.append(count)
            new_say = ''
            for i in range(len(buff)):
                new_say += str(count_buff[i])
                new_say += str(buff[i])
            say = new_say
        return say