class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # state is index of s1, s2, s3
        if len(s1) + len(s2) != len(s3):
            return False
        
        prev = []
        state = [0, 0, 0]
        states = [state]
        
        while len(states) > 0:
            state = states.pop(0)
            if state not in prev:
                prev.append(state)
                state = [state[0], state[1], state[2]]
                i1 = state[0]
                i2 = state[1]
                i3 = state[2]


                if i1 == len(s1):
                    while i2 < len(s2):
                        if s2[i2] != s3[i3]:
                            break
                        i2 += 1
                        i3 += 1
                    if i2 == len(s2):
                        return True

                elif i2 == len(s2):
                    while i1 < len(s1):
                        if s1[i1] != s3[i3]:
                            break
                        i1 += 1
                        i3 += 1
                    if i1 == len(s1):
                        return True


                elif s1[i1] == s2[i2] and s1[i1] == s3[i3]:
                    #do both
                    state1 = [state[0], state[1], state[2]]
                    state2 = [state[0], state[1], state[2]]
                    #1
                    i1 = state1[0]
                    i2 = state1[1]
                    i3 = state1[2]
                    while s1[i1] == s3[i3] and s1[i1] == s2[i2]:
                        i1 += 1
                        i3 += 1
                        if i1 == len(s1):
                            break
                    state1[0] = i1
                    state1[2] = i3
                    states.append(state1)
                    #2
                    i1 = state2[0]
                    i2 = state2[1]
                    i3 = state2[2]
                    while s2[i2] == s3[i3] and s1[i1] == s2[i2]:
                        i2 += 1
                        i3 += 1
                        if i2 == len(s2):
                            break
                    state2[1] = i2
                    state2[2] = i3
                    states.append(state2)

                elif s1[i1] == s3[i3]:
                    state[0] += 1
                    state[2] += 1
                    states.append(state)

                elif s2[i2] == s3[i3]:
                    state[1] += 1
                    state[2] += 1
                    states.append(state)
        return False
