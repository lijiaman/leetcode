class Solution:
    def simplifyPath(self, path: str) -> str:
        s_list = path.split('/')
        str_list = []
        for s in s_list:
            if s != '' and s != '.':
                str_list.append(s)

        stack = []
        for i in range(len(str_list)):
            if str_list[i] == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(str_list[i])

        return '/' + '/'.join(stack)

