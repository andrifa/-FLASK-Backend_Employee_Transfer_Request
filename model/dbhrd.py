from app import db

class EmployeeData(db.Model):
    __tablename__ = 'employeedata'

    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String())
    position_code = db.Column(db.String())
    position = db.Column(db.String())
    company = db.Column(db.String())
    costcntr_id = db.Column(db.String())
    costcntr_name = db.Column(db.String())
    personal_area = db.Column(db.String())
    employee_group = db.Column(db.String())
    employee_subgroup = db.Column(db.String())


    def __init__(self, employee_name, position_code, position, company, costcntr_id, costcntr_name, personal_area, employee_group, employee_subgroup):
        self.employee_name = employee_name
        self.position_code = position_code
        self.position = position
        self.company = company
        self.costcntr_id = costcntr_id
        self.costcntr_name = costcntr_name
        self.personal_area = personal_area
        self.employee_group = employee_group
        self.employee_subgroup = employee_subgroup
    
    def serialize(self):
        return {
            'employee_id':self.employee_id,
            'employee_name':self.employee_name,
            'position_code':self.position_code,
            'position':self.position,
            'company':self.company,
            'costcntr_id':self.costcntr_id,
            'costcntr_name':self.costcntr_name,
            'personal_area':self.personal_area,
            'employee_group':self.employee_group,
            'employee_subgroup':self.employee_subgroup
            }

class JobData(db.Model):
    __tablename__ = 'jobdesc'

    job_id = db.Column(db.Integer, primary_key=True)
    position_code = db.Column(db.String())
    position = db.Column(db.String())
    company = db.Column(db.String())
    cost_center_id = db.Column(db.String())
    cost_center_name = db.Column(db.String())
    personal_area = db.Column(db.String())
    employee_group = db.Column(db.String())
    employee_subgroup = db.Column(db.String())
    dcost_center_id = db.Column(db.String())
    dcost_center_name = db.Column(db.String())
    employee_type = db.Column(db.String())
    personal_subarea = db.Column(db.String())


    def __init__(self, position_code, position, company, cost_center_id, cost_center_name, 
    personal_area, employee_group, employee_subgroup, dcost_center_id, dcost_center_name, employee_type, personal_subarea):
        self.position_code = position_code
        self.position = position
        self.company = company
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.personal_area = personal_area
        self.employee_group = employee_group
        self.employee_subgroup = employee_subgroup
        self.dcost_center_id = dcost_center_id
        self.dcost_center_name = dcost_center_name
        self.employee_type = employee_type
        self.personal_subarea = personal_subarea
    
    def serialize(self):
        return {
            'job_id':self.job_id,
            'position_code':self.position_code,
            'position':self.position,
            'company':self.company,
            'cost_center_id':self.cost_center_id,
            'cost_center_name':self.cost_center_name,
            'personal_area':self.personal_area,
            'employee_group':self.employee_group,
            'employee_subgroup':self.employee_subgroup,
            'dcost_center_id':self.dcost_center_id,
            'dcost_center_name':self.dcost_center_name,
            'employee_type':self.employee_type,
            'personal_subarea':self.personal_subarea
            }

class RequestData(db.Model):
    __tablename__ = 'myrequest'

    request_id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.String())
    process_id = db.Column(db.String())
    req_name = db.Column(db.String())
    req_npk = db.Column(db.String())
    req_position = db.Column(db.String())
    ob_name = db.Column(db.String())
    ob_position = db.Column(db.String())
    e_id = db.Column(db.String())
    e_name = db.Column(db.String())
    e_poscode = db.Column(db.String())
    e_position = db.Column(db.String())
    e_company = db.Column(db.String())
    e_costid = db.Column(db.String())
    e_costname = db.Column(db.String())
    e_perarea = db.Column(db.String())
    e_group = db.Column(db.String())
    e_subgroup = db.Column(db.String())
    types = db.Column(db.String())
    poscode = db.Column(db.String())
    position = db.Column(db.String())
    costid = db.Column(db.String())
    costname = db.Column(db.String())
    dcostid = db.Column(db.String())
    dcostname = db.Column(db.String())
    company = db.Column(db.String())
    perarea = db.Column(db.String())
    persubarea = db.Column(db.String())
    em_type = db.Column(db.String())
    receiver = db.Column(db.String())
    em_date = db.Column(db.String())
    attach = db.Column(db.String())
    justif = db.Column(db.String())

    def __init__(self, record_id, process_id, req_name, req_npk,
    req_position, ob_name, ob_position, e_id, e_name, e_poscode,
    e_position, e_company, e_costid, e_costname, e_perarea, e_group, 
    e_subgroup, types, poscode, position, costid, costname, dcostid,
    dcostname, company, perarea, persubarea, em_type, receiver, em_date, attach, justif):
        self.record_id = record_id
        self.process_id = process_id
        self.req_name = req_name
        self.req_npk = req_npk
        self.req_position = req_position
        self.ob_name = ob_name
        self.ob_position = ob_position
        self.e_id = e_id
        self.e_name = e_name
        self.e_poscode = e_poscode
        self.e_position = e_position
        self.e_company = e_company
        self.e_costid = e_costid
        self.e_costname = e_costname
        self.e_perarea = e_perarea
        self.e_group = e_group
        self.e_subgroup = e_subgroup
        self.types = types
        self.poscode = poscode
        self.position = position
        self.costid = costid
        self.costname = costname
        self.dcostid = dcostid
        self.dcostname = dcostname
        self.company = company
        self.perarea = perarea
        self.persubarea = persubarea
        self.em_type = em_type
        self.receiver = receiver
        self.em_date = em_date
        self.attach = attach
        self.justif = justif
    
    def serialize(self):
        return {
            'request_id':self.request_id,
            'record_id':self.record_id,
            'process_id':self.process_id,
            'req_name':self.req_name,
            'req_npk':self.req_npk,
            'req_position':self.req_position,
            'ob_name':self.ob_name,
            'ob_position':self.ob_position,
            'e_id':self.e_id,
            'e_name':self.e_name,
            'e_poscode':self.e_poscode,
            'e_position':self.e_position,
            'e_company':self.e_company,
            'e_costid':self.e_costid,
            'e_costname':self.e_costname,
            'e_perarea':self.e_perarea,
            'e_group':self.e_group,
            'e_subgroup':self.e_subgroup,
            'types':self.types,
            'poscode':self.poscode,
            'position':self.position,
            'costid':self.costid,
            'costname':self.costname,
            'dcostid':self.dcostid,
            'dcostname':self.dcostname,
            'company':self.company,
            'perarea':self.perarea, 
            'persubarea':self.persubarea,
            'em_type':self.em_type,
            'receiver':self.receiver,
            'em_date':self.em_date,
            'attach':self.attach,
            'justif':self.justif
            }

class CreateHistory(db.Model):
    __tablename__ = 'createHistory'

    id_create = db.Column(db.Integer, primary_key=True)
    creatorId = db.Column(db.String())
    creatorName = db.Column(db.String())
    record_id = db.Column(db.String())
    process_id = db.Column(db.String())

    def __init__(self, creatorId, creatorName, record_id, process_id):
        self.creatorId = creatorId
        self.creatorName = creatorName
        self.record_id = record_id
        self.process_id = process_id
    
    def serialize(self):
        return {
            'id_create':self.id_create,
            'creatorId':self.creatorId,
            'creatorName':self.creatorName,
            'record_id':self.record_id,
            'process_id':self.process_id
            }

class ComHistory(db.Model):
    __tablename__ = 'comHistory'

    id_history = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.String())
    record_id = db.Column(db.String())
    created_at = db.Column(db.String())
    completed_at = db.Column(db.String())
    name = db.Column(db.String())
    position = db.Column(db.String())
    response = db.Column(db.String())
    comment = db.Column(db.String())

    def __init__(self, task_id, record_id, created_at, completed_at, name, position, response, comment):
        self.task_id = task_id
        self.record_id = record_id
        self.created_at = created_at
        self.completed_at = completed_at
        self.name = name
        self.position = position
        self.response = response
        self.comment = comment
    
    def serialize(self):
        return {
            'id_history':self.id_history,
            'task_id':self.task_id,
            'record_id':self.record_id,
            'created_at':self.created_at,
            'completed_at':self.completed_at,
            'name':self.name,
            'position':self.position,
            'response':self.response,
            'comment':self.comment
            }