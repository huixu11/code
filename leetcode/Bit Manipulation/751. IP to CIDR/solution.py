    class Solution:
        def ipToCIDR(self, ip: str, n: int) -> List[str]:
            # # 32-3=29
            # # 8 = 2^3
            # # 255.0.0.16/32
            # # n = 10
            # find the last 1's position of the ip address binary representation min(1, 10) = 0
            # 32 - 1 + 1 = 32
            # 255.0.0.7/32
            # 255.0.0.7+1 = 255.0.0.8
            # the last 1 position 4 min(4, 10-1) = 3, 32-4+1=29
            # 255.0.0.8/29
            # 2^3  n-1-2^3=1
            # 255.0.0.8+2^3 = 255.0.0.16
            # the last 1 positon 4 min(3, 1) = 1, 32-1+1=32
            def ip_to_int(ip):
                ip_strs = ip.split('.')
                return (int(ip_strs[0]) << 24) + (int(ip_strs[1]) << 16) + (int(ip_strs[2]) << 8) + int(ip_strs[3])
            
            def int_to_ip(ip_int):
                res = []
                for i in range(24, -1, -8):
                    tmp_val = ip_int >> i
                    res.append(str(tmp_val))
                    ip_int -= ((tmp_val) << i)
                return '.'.join(res)

            res = []

            start = ip_to_int(ip)
            while n > 0:
                if start == 0:
                    last_1_pos = 32
                else:
                    last_1_pos = start & (-start)
                    last_1_pos = last_1_pos.bit_length()
                count = min(last_1_pos, n.bit_length())
                pref_num = 32 - count + 1
                res.append(int_to_ip(start) + '/' + str(pref_num))
                tmp = pow(2, count-1)
                start += tmp
                n -= tmp
            return res
