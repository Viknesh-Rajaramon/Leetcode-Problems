class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        op, stack = [], []
        def ope():
            l, r = len(stack)-2, len(stack)-1
            if op[-1] == '+':
                stack[l] |= stack[r]
            else:
                tmp = set()
                for left in stack[l]:
                    for right in stack[r]:
                        tmp.add(left+right)
                
                stack[l] = tmp
            
            op.pop()
            stack.pop()
        
        for i, c in enumerate(expression):
            if c == ',':
                while op and op[-1] == '*':
                    ope()
                
                op.append('+')
            elif c == '{':
                if i > 0 and (expression[i-1] == '}' or expression[i-1].isalpha()):
                    op.append('*')
                
                op.append('{')
            elif c == '}':
                while op and op[-1] != '{':
                    ope()
                
                op.pop()
            else:
                if i > 0 and (expression[i-1] == '}' or expression[i-1].isalpha()):
                    op.append('*')
                
                stack.append({c})
        
        while op:
            ope()
        
        return sorted(stack[-1])
