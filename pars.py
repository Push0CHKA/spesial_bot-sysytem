from mods.pars import worker
from mods.analys import users_analys
from mods import diff

token = 'ea5514cc4168826ca6a60f4227e37ebfb754f743154f1de717572c88aae0ce81b882a166ed719642d6a15'
groups_ids = [55206187]
new_tipash = 'noviy_tipash_1'

#worker.download_users_ids(token, groups_ids)
#worker.download_users_data(token)

diff.make_prob_db(new_tipash)
users_analys.make_first_names_prob(new_tipash)
users_analys.make_last_names_prob(new_tipash)


