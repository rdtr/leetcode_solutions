class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        enteringBlockComment = False
        
        res = []
        newChs = []
        enteringBlockComment = False
        shouldAddNewLine = True
        i = 0
        while i < len(source):
            line = source[i]            
            j = 0
            while j < len(line):
                ch = line[j]
                
                if self.doubleSlash(j, line):
                    if not enteringBlockComment:
                        shouldAddNewLine = True
                        break
                    j += 1
                elif self.isCloseBlockCommentStr(j, line):
                    if enteringBlockComment:
                        enteringBlockComment = False
                        j += 2
                    else:
                        newChs.append(ch)
                        j += 1
                elif self.isOpenBlockCommentStr(j, line):
                    if not enteringBlockComment:
                        enteringBlockComment = True
                        j += 2
                    else:
                        j += 1
                elif enteringBlockComment:
                    j += 1
                else:
                    newChs.append(ch)
                    j += 1
                shouldAddNewLine = not enteringBlockComment and j == len(line)
            
            if shouldAddNewLine and newChs:
                res.append(''.join(newChs))
                newChs = [] # reset
            i += 1
        return res
                
    def isOpenBlockCommentStr(self, i, line):
        return line[i] == '/' and i + 1 < len(line) and line[i+1] == '*'
    
    def isCloseBlockCommentStr(self, i, line):
        return line[i] == '*' and i + 1 < len(line) and line[i+1] == '/'
            
    def doubleSlash(self, i, line):
        return line[i] == '/' and i + 1 < len(line) and line[i+1] == '/'