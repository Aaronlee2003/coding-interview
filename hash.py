class HashTable:
    def __init__(self, size=10):
        self.size = size
        # 충돌 해결을 위해 각 방을 빈 리스트(Chaining용)로 초기화합니다.
        self.table = [[] for _ in range(self.size)]

    def _hashfunction(self,key):
        return hash(key)%self.size
    def put(self,key,value):
        index=self._hashfunction(key)
        bucket=self.table(index)
        for i,(k,v) in enumerate(bucket):#특정 버킷에 몇번째에 값이 존재하는지 체크
            if k==key:
                bucket[i]=(key,value)# i번쨰 에 있던 값을 수정함
                return
        bucket.append((key,value))# 값이 없으면 투입
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.table[index]
        for k,v in bucket:
            if k==key:
                return v
            else:
                KeyError(f"Key '{key}'를 찾을 수 없습니다.")
        def remove (self.key):
            index=self._hashfunction(key)
            bucket=self.table[index]

            for i,(k,v) in enumerate(bucket):
                if k==key:
                    del bucket[i]
                    return
            raise KeyError(f"Key '{key}'를 찾을 수 없습니다.")
        def __str__(self):
            result=[]
            for i, bucket in enumerate(self.table):
              result.append(f"Bucket {i}: {bucket}")
        return "\n".join(result)
            
                
        