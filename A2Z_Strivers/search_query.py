#User function Template for python3

class AutoCompleteSystem():
    
    MAX_LEN = 3
    
    def __init__(self, sentences, times):
        # write code for constructor
        self.search_query = ""
        self.search_history = {}
        self.cur_search = {}
        for sentence, count in zip(sentences, times):
            self.search_history[sentence] = count
    
    def input(self,c):
        '''
            write code to return the top 3 suggestions when the current character in the stream is c
            c == '#' means , the current query is complete and you may save the entire query into
            historical data
        '''
        if c == "#":
            self.search_history[self.search_query] = self.search_history.get(self.search_query, 0) + 1
            self.search_query = ""
            self.cur_search = {}
            return
        
        self.search_query += c
        self.cur_search = {}
        for key, value in self.search_history.items():
            if key.startswith(self.search_query):
                self.cur_search.setdefault(value, [])
                self.cur_search[value].append(key)
        
        keys = list(self.cur_search.keys())
        keys.sort(reverse=True)  
        result = []
        for key in keys:
            if 0 >= len(self.cur_search[key]):
                continue
            
            # if len(self.cur_search[key]) >= self.MAX_LEN - len(result):
            temp = self.cur_search[key]
            temp.sort()
            result += temp[:self.MAX_LEN - len(result)]
            if len(result) >= self.MAX_LEN:
                break
            
        return result
                

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        sentences = ["ijkl",
                    "i hate maths",
                    "i love gfg",
                    "i love geeksforgeeks",
                    "i love gaming",
                    "i lob gfg",
                    "i lov geeksforgeeks"]
        times = [100, 90, 5, 3, 5, 99, 12]
        # for _ in range(n):
        #     sentence = input()
        #     sentences.append(sentence)
        #     time = int(input())
        #     times.append(time)

        obj = AutoCompleteSystem(sentences, times)

        q = ["i love gfg#",
            "i lob gfg#",
            "i lov gfg#",
            "i like gfg#",
            "i like gfg#",
            "i like gfg#",
            "i like gfg#"]
        for query in q:
            qq = ""
            for x in query:
                qq += x
                suggestions = obj.input(x)
                if x == '#':
                    continue
                print('Typed : "' + qq + '" , Suggestions:')
                for y in suggestions:
                    print(y)

        t -= 1

# } Driver Code Ends