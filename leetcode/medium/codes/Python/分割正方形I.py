class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for xi, yi, li in squares:
            start_y = yi
            end_y = yi + li
            events.append((start_y, 'start', yi, li))
            events.append((end_y, 'end', yi, li))
    
        events.sort(key=lambda x: x[0])
    
        sum1 = 0
        sum2 = sum(li ** 2 for xi, yi, li in squares)
        sum3_C = 0
        sum3_D = 0
        ans = float('inf')
        prev_y = None
    
        for event in events:
            y_val, typ, yi, li = event
        
            if prev_y is not None and y_val > prev_y:
                C = sum1 - sum2 + sum3_C
                D = sum3_D
                if D == 0:
                    if C == 0 and prev_y < ans:
                        ans = prev_y
                else:
                    k_candidate = -C / D
                    if prev_y <= k_candidate < y_val:
                        if k_candidate < ans:
                            ans = k_candidate
        
            if typ == 'start':
                sum2 -= li ** 2
                delta_C = (-2 * yi - li) * li
                sum3_C += delta_C
                sum3_D += 2 * li
            else:
                delta_C = (-2 * yi - li) * li
                sum3_C -= delta_C
                sum3_D -= 2 * li
                sum1 += li ** 2
        
            prev_y = y_val
    
        C = sum1 - sum2 + sum3_C
        D = sum3_D
        if D == 0 and C == 0 and prev_y < ans:
            ans = prev_y
    
        return ans
        