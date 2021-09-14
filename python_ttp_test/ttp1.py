from ttp import ttp
import raw_data
import ttp_template


parser = ttp(data=raw_data.ospf_raw1, template=ttp_template.ospf_ttp)
parser.parse()
result = parser.result(format='json')[0]
print(result)
