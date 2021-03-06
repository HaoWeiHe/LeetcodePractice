class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(node):
            for i in xrange(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1

import collections
class Solution(object):
	def openLock(self, deadends, target):
		start = "0000"
		deadends = set(deadends)
		if start in deadends: return -1
		
		q = collections.deque(([(start,0)]))
		
		record = set()
		
		while q:
			top, times = q.popleft()

			if  top  == target: return times
			
			for i in range(4):
				for val in [1,-1]: 
					candidate =  top[:i] + str((int(top[i]) + val) %10 ) + top[i+1:] 
					if candidate in record: continue
					record.add(candidate)
					if candidate in deadends: continue
					q.append((candidate, times+1))
		return -1

deadends =["1041","8846","8013","0993","8148","3810","2537","1480","8757","9849","0141","6866","4721","3752","0884","3832","5452","1312","7734","4922","8341","8629","7054","9541","1101","5936","8155","2485","1743","2402","0542","7189","8251","8345","7233","2730","5806","8830","5955","8704","4439","0615","2482","5273","8134","8421","6389","9495","3982","3480","5338","3174","5964","9706","0831","5594","2823","1924","3245","6358","3779","6895","8971","9499","9633","9919","2149","0677","2377","9337","9015","6745","5350","9424","7978","9566","5322","7890","1629","8485","4251","7065","2371","0644","7918","2227","8546","1690","2615","7910","0637","5604","7777","1470","8393","1604","5135","5120","9203","2633","3380","4087","0529","3269","5470","1869","3223","8642","3606","1445","0447","2510","3769","8089","7233","1829","8945","3317","7752","8246","2855","0363","4920","8460","9706","8744","2261","5953","4707","8613","7974","4000","1400","4340","7655","5983","7574","8868","4801","3630","2081","0563","2106","6809","6461","9175","4015","1190","4671","1363","5971","3839","7745","0928","8365","4467","1306","5758","5378","1709","2914","3184","3010","6521","3293","0917","0928","3960","7313","0310","3138","7672","8096","5337","2776","9488","7535","6389","8583","6135","5668","3383","8455","8128","2380","2908","5419","5327","6154","1556","1353","6993","2743","8303","8732","5256","5051","8128","4192","9281","6663","2166","2942","2004","6426","2149","7197","3422","6475","5708","6828","9930","3255","4026","9506","7392","7943","6337","5551","2928","6767","0251","8662","2644","1644","0021","9614","1768","5947","7935","5192","9890","7793","9854","4855","3241","7438","6352","9514","8456","7621","6565","9829","3422","0140","9056","1346","6859","9056","5457","7428","1865","5092","2788","8104","7168","0942","8736","3942","9007","8969","1987","2361","2404","4781","5824","0879","0683","5069","1450","9345","5696","9920","0885","1130","4285","1330","0007","6405","2957","9182","2704","6667","6082","8833","5406","9231","1428","4326","5522","6824","7864","9589","8479","3442","2322","6185","1457","4564","7376","7922","6241","8718","7042","2265","9780","4187","7673","0485","5830","4603","2933","1801","6342","5958","8126","4969","1846","1723","7211","2943","6668","0171","1783","0319","8441","6265","0288","8541","5132","5889","0265","0983","8618","1731","7605","6930","4711","9875","8588","9108","0517","8863","0343","6282","5834","0091","7394","8728","5745","0178","9320","8727","8312","2986","7110","5694","6662","8649","4902","1572","6595","3845","8130","7726","6038","9289","0117","8361","9492","0588","4375","2441","1731","8225","6095","3348","3133","7667","3660","6930","6260","0023","8761","4094","5157","9682","7581","4179","2193","4703","2505","0696","6391","5130","8318","6194","4009","2225","4561","6623","8769","7046","6053","3196","4397","5519","3102","4406","3307","7955","7521","8842","6309","7077","1345","0366","4839","1213","2512","7771","6217","4556","6874","8926","2189","2612","3352","5510","3219","6292","4125","5861","0846","0405","3160","5546","2497","2310","8269","2957","3972","0815","5155","4188","0686","8384","4266","4029","0756","8474","2028","3559","9940","8232","9058","9392","2450","0092","5500","8650","5355","2554","9876","1600","7004","3622","0938","6226","8364","4593","0209","1781","8889","3672","3818","2552","9866","2099","0790","2980","5507","0873","3778","5919","2172","3701","3405","4059","9408","5483","2933","1191","0056","9076","4060","5659","0955","1468","1402"]
"6023"# ["0201","0101","0102","1212","2002"]
target = "0202"
Solution().openLock(deadends, target)