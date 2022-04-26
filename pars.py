from mods.pars import worker
from mods.analys import users_analys
from mods import db
from config.db_config import prob_first_names_db_fields, prob_female_first_names_db_tname, \
    prob_male_first_names_db_tname, prob_db_path, prob_male_last_names_db_tname, prob_female_last_names_db_tname, \
    prob_last_names_db_fields

token = 'ea5514cc4168826ca6a60f4227e37ebfb754f743154f1de717572c88aae0ce81b882a166ed719642d6a15'
groups_ids = [55206187]
new_tipash = 'noviy_tipash_1'

#worker.download_users_ids(token, groups_ids)
#worker.download_users_data(token)
db.make_db(prob_db_path + '/' + new_tipash + '.db', prob_female_first_names_db_tname, prob_first_names_db_fields)
db.make_db(prob_db_path + '/' + new_tipash + '.db', prob_male_first_names_db_tname, prob_first_names_db_fields)
users_analys.make_first_names_prob(new_tipash)

db.make_db(
    prob_db_path + '/' + new_tipash + '.db',
    prob_male_last_names_db_tname,
    prob_last_names_db_fields
)
db.make_db(
    prob_db_path + '/' + new_tipash + '.db',
    prob_female_last_names_db_tname,
    prob_last_names_db_fields
)
users_analys.make_last_names_prob(new_tipash)


