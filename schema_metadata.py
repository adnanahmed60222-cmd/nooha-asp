# Auto-generated schema metadata

SCHEMA_METADATA = {
    'applicationcontactdetails': {
        'columns': [
            {
                'name': 'applicationcontactdetailsid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'contacttypeid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'telephonetypeid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'telephonenumber',
                'type': 'character varying',
                'examples': ['01234556666', '0123654789', '08264579227', '08489573090', '+0987654321'],
            },
            {
                'name': 'applicantname',
                'type': 'character varying',
                'examples': ['abccc', 'ahila', 'ahila.godbin', 'AN23', 'applicationasd'],
            },
            {
                'name': 'emailid',
                'type': 'character varying',
                'examples': ['abc@gmail.com', 'ahila.godbin@nooha-asp.com', 'aq@gmail.com', 'de@gmail.com', 'dgrt@gmail.com'],
            },
        ]
    },
    'applicationcountries': {
        'columns': [
            {
                'name': 'applicationcountryid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'countryid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'inventedname',
                'type': 'character varying',
                'examples': ['', 'CroBH', 'fhfh', 'frgsfg', 'gdfgdfh'],
            },
            {
                'name': 'inn',
                'type': 'character varying',
                'examples': ['', '2', '45', '56', 'bbb'],
            },
        ]
    },
    'applicationcrossreferences': {
        'columns': [
            {
                'name': 'applicationcrossreferencesid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'crossreferenceapplicationnumber',
                'type': 'character varying',
                'examples': ['', '036127', '036128', '06666', '090909'],
            },
            {
                'name': 'crossreferenceapplicationtype',
                'type': 'character varying',
                'examples': [''],
            },
            {
                'name': 'crossreferenceapplicationtypeid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'rowcrossapplicationtype',
                'type': 'character varying',
                'examples': ['jhjuhg', 'testing'],
            },
        ]
    },
    'applications': {
        'columns': [
            {
                'name': 'applicationid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'principalproductid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'accountid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationtypeid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'healthauthority',
                'type': 'character varying',
                'examples': ['EMA', 'EUROPE', 'European Medicines Agency', 'FDA', 'Food and Drug Administration'],
            },
            {
                'name': 'applicationnumberavailable',
                'type': 'boolean',
                'examples': [],
            },
            {
                'name': 'projectidentifier',
                'type': 'character varying',
                'examples': ['', '3.3', '66', '7', 'abcds'],
            },
            {
                'name': 'applicationnumber',
                'type': 'character varying',
                'examples': ['000111', '000456', '000888', '000890', '001100'],
            },
            {
                'name': 'dunsnumber',
                'type': 'character varying',
                'examples': ['', '0000000', '012345678', '012345698', '012365478'],
            },
            {
                'name': 'companyname',
                'type': 'character varying',
                'examples': ['abcbabc', 'Amneal EU, Limited', 'cipla', 'CN12', 'companyasd'],
            },
            {
                'name': 'createddatetime',
                'type': 'timestamp with time zone',
                'examples': [],
            },
            {
                'name': 'modifiedby',
                'type': 'character varying',
                'examples': ['adarsh', 'dyadmin13', 'dyauthor13', 'dyaz', 'dyaz1'],
            },
            {
                'name': 'isactive',
                'type': 'boolean',
                'examples': [],
            },
            {
                'name': 'lastupdateddatetime',
                'type': 'timestamp with time zone',
                'examples': [],
            },
            {
                'name': 'uuid',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'submissionformat',
                'type': 'character varying',
                'examples': ['ctd', 'CTD', 'ectd', 'eCTD'],
            },
            {
                'name': 'rowapplicationtype',
                'type': 'character varying',
                'examples': ['AT2', 'init', 'jhjuhg', 'NDA-APP', 'testing'],
            },
        ]
    },
    'applicationtypes': {
        'columns': [
            {
                'name': 'applicationtypeid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationtypecode',
                'type': 'character varying',
                'examples': ['app-type-1', 'app-type-2', 'app-type-3', 'app-type-4', 'app-type-5'],
            },
            {
                'name': 'applicationtypevalue',
                'type': 'character varying',
                'examples': ['Abbreviated New Drug Application', 'Biologic License Application', 'Centralised', 'Centralised Procedure', 'De Centralised'],
            },
            {
                'name': 'createddate',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'obsoleteddate',
                'type': 'timestamp without time zone',
                'examples': [],
            },
        ]
    },
    'auditlogs': {
        'columns': [
            {
                'name': 'auditlogid',
                'type': 'bigint',
                'examples': [],
            },
            {
                'name': 'accountid',
                'type': 'bigint',
                'examples': [],
            },
            {
                'name': 'userid',
                'type': 'bigint',
                'examples': [],
            },
            {
                'name': 'logdatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'username',
                'type': 'character varying',
                'examples': ['adarsh', 'adminuser12', 'dyadmin13', 'dyauthor13', 'dyaz'],
            },
            {
                'name': 'objecttype',
                'type': 'character varying',
                'examples': ['Account', 'Announcement', 'Application', 'Audit', 'audit-log'],
            },
            {
                'name': 'activity',
                'type': 'character varying',
                'examples': ['Added Document', 'Added Folder', 'Added Template Document', 'Added Template Folder', 'Create Account'],
            },
            {
                'name': 'requestjson',
                'type': 'text',
                'examples': ['"009911"', '"020304"', '"030901"', '"123456"', '"2111112"'],
            },
            {
                'name': 'responsejson',
                'type': 'text',
                'examples': ['[ ]', '{\n  "accountId" : 12,\n  "accountName" : "DyazAccount",\n  "active" : true,\n  "contactPerson" : "Test1",\n  "contactNumber" : "+917418529630",\n  "designation" : "Admin",\n  "email" : "dyazadmin@gmail.com",\n  "companyAddress" : "hyderabad",\n  "website" : "www.dyazinnovate.com",\n  "message" : "logo uploaded successfully"\n}', '{\n  "accountId" : 13,\n  "accountName" : "DyazProd",\n  "active" : true,\n  "contactPerson" : "Sadiya",\n  "contactNumber" : "+91987456321",\n  "designation" : "RA Head",\n  "email" : "sadiya.parveen@nooha-asp.com",\n  "companyAddress" : "Hyderabad",\n  "website" : "www.dyazinnovate.com",\n  "message" : "logo uploaded successfully"\n}', '{\n  "accountId" : 14,\n  "accountName" : "dyaz123",\n  "active" : true,\n  "contactPerson" : "adarsh",\n  "contactNumber" : "+917766889954",\n  "designation" : "dev",\n  "email" : "adarsh.malavade@nooha.asp.com",\n  "companyAddress" : "Hydrabad",\n  "website" : "www.dyazinnovate.com",\n  "message" : "logo uploaded successfully"\n}', '{\n  "accountId" : 15,\n  "accountName" : "DyazProd-2",\n  "active" : true,\n  "contactPerson" : "Sadiya",\n  "contactNumber" : "9874563210",\n  "designation" : "RA Head",\n  "email" : "sadiya.parveen@nooha-asp.com",\n  "companyAddress" : "Hyderabad",\n  "website" : "www.dyazinnovate.com",\n  "message" : "logo uploaded successfully"\n}'],
            },
        ]
    },
    'contacttypes': {
        'columns': [
            {
                'name': 'contacttypeid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'contacttypecode',
                'type': 'character varying',
                'examples': ['contact-type-1', 'contact-type-2', 'contact-type-3', 'contact-type-4', 'contact-type-5'],
            },
            {
                'name': 'contacttypevalue',
                'type': 'character varying',
                'examples': ['General', 'Local Applicant', 'Product Information', 'Promotional Labeling and Advertising Regulatory Contact', 'Regulatory'],
            },
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'createddate',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'obsoleteddate',
                'type': 'timestamp without time zone',
                'examples': [],
            },
        ]
    },
    'countries': {
        'columns': [
            {
                'name': 'countryid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'countrycode',
                'type': 'character varying',
                'examples': ['AE', 'AT', 'BE', 'bf', 'BG'],
            },
            {
                'name': 'countryname',
                'type': 'character varying',
                'examples': ['Austria', 'Bahrain', 'Belgium', 'Benin', 'Bulgaria'],
            },
            {
                'name': 'agencycode',
                'type': 'character varying',
                'examples': ['ABRP', 'AE-MOH', 'AIRP', 'ANRP', 'ARP'],
            },
            {
                'name': 'agencyname',
                'type': 'character varying',
                'examples': ['Agency for Medicinal Products and Medical Devices of Croatia', 'Agency for Medicinal Products and Medical Devices of the Republic of Slovenia', 'Austrian Federal Office for Safety in Health Care/Austrian Medicines and Medical Devices Agency', 'Benin-ABRP', 'Bulgarian Drug Agency'],
            },
        ]
    },
    'databasechangelog': {
        'columns': [
            {
                'name': 'id',
                'type': 'character varying',
                'examples': ['05', '06', '1', '10', '11'],
            },
            {
                'name': 'author',
                'type': 'character varying',
                'examples': ['adarsh', 'imran', 'jyothi', 'kalash', 'shazia'],
            },
            {
                'name': 'filename',
                'type': 'character varying',
                'examples': ['/db/changelog/changes/alter-application.sql', '/db/changelog/changes/alter-applicationtypes.sql', '/db/changelog/changes/alter-crossreferenceapplication.sql', '/db/changelog/changes/alter-ecowassubmissionrule.sql', '/db/changelog/changes/alter-filedetail.sql'],
            },
            {
                'name': 'dateexecuted',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'orderexecuted',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'exectype',
                'type': 'character varying',
                'examples': ['EXECUTED'],
            },
            {
                'name': 'md5sum',
                'type': 'character varying',
                'examples': ['8:017a3621a16be3655ca7538a9e0566c1', '8:06c393bdf62a7b851695f695387058ec', '8:0730aef75ae5d31816a96d210aa7bf5e', '8:0ab49c82c5c06003c0cf4b2fe9161cf5', '8:0b8e40ae9ffd3e648834262f60969abc'],
            },
            {
                'name': 'description',
                'type': 'character varying',
                'examples': ['sql'],
            },
            {
                'name': 'comments',
                'type': 'character varying',
                'examples': ['', 'add-accountid-column-to-queries', 'Add checksum column', 'add createdDate, obsoletedDate to submissiontypes,submissionsubtypes,applicationtypes,contacttypes', 'added table application'],
            },
            {
                'name': 'tag',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'liquibase',
                'type': 'character varying',
                'examples': ['3.8.9'],
            },
            {
                'name': 'contexts',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'labels',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'deployment_id',
                'type': 'character varying',
                'examples': ['0068763928', '0154558434', '0176569501', '0405018223', '0407466074'],
            },
        ]
    },
    'databasechangeloglock': {
        'columns': [
            {
                'name': 'id',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'locked',
                'type': 'boolean',
                'examples': [],
            },
            {
                'name': 'lockgranted',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'lockedby',
                'type': 'character varying',
                'examples': [],
            },
        ]
    },
    'documentmatrix': {
        'columns': [
            {
                'name': 'code',
                'type': 'character varying',
                'examples': ['E', 'NV', 'NYD', 'P', 'W'],
            },
            {
                'name': 'value',
                'type': 'character varying',
                'examples': ['Error', 'Excluded: Error', 'Excluded: Warning', 'Not Validated', 'Not Yet Defined'],
            },
            {
                'name': 'description',
                'type': 'character varying',
                'examples': ['Not yet planned within the scope of the eCTD.', 'The document is expected in the sequence. If no document is present, it will lead to a warning and could possibly lead to the sequence being rejected.', 'The document is not allowed for the particular Submission Type and will result in an Error if included.', 'The document is not expected for the particular Submission Type and will result in a Warning if included.', 'The document is required in certain circumstances for the particular sequence type, but not all. A list of the sections where content has been provided will be created by the validator for review purposes in content screening. The absence of a required document could lead to the sequence being rejected.'],
            },
        ]
    },
    'documenttasks': {
        'columns': [
            {
                'name': 'id',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'fileid',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'filepath',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'documentname',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'sequenceid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationnumber',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'author',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'approver',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'reviewer',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'authortargetdate',
                'type': 'timestamp with time zone',
                'examples': [],
            },
            {
                'name': 'reviewertargetdate',
                'type': 'timestamp with time zone',
                'examples': [],
            },
            {
                'name': 'approvertargetdate',
                'type': 'timestamp with time zone',
                'examples': [],
            },
            {
                'name': 'prioritydate',
                'type': 'timestamp with time zone',
                'examples': [],
            },
            {
                'name': 'status',
                'type': 'character varying',
                'examples': [],
            },
        ]
    },
    'dtdmapping': {
        'columns': [
            {
                'name': 'dtdmappingid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'utilfileid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'elementname',
                'type': 'character varying',
                'examples': ['m1-0-1-application-letter', 'm1-0-1-cover-letter', 'm1-0-2-note-to-evaluator', 'm1-0-2-reviewer-note', 'm1-0-3-correspondence-from-authority'],
            },
            {
                'name': 'sourcefoldername',
                'type': 'character varying',
                'examples': ['1.0.1 Cover Letter', '1.0.1 Letter of Application', '1.0.2 General Note to Reviewer', '1.0.2 Note to Evaluator', '1.0.3 Correspondence from SAHPRA'],
            },
        ]
    },
    'ecowasdocumentmatrix': {
        'columns': [
            {
                'name': 'code',
                'type': 'character varying',
                'examples': ['E', 'NV', 'NYD', 'P', 'W'],
            },
            {
                'name': 'value',
                'type': 'character varying',
                'examples': ['Error', 'Excluded: Error', 'Excluded: Warning', 'Not Validated', 'Not Yet Defined'],
            },
            {
                'name': 'description',
                'type': 'character varying',
                'examples': ['Not yet planned within the scope of the eCTD.', 'The document is expected in the sequence. If no document is present, it will lead to a warning and could possibly lead to the sequence being rejected.', 'The document is not allowed for the particular Submission Type and will result in an Error if included.', 'The document is not expected for the particular Submission Type and will result in a Warning if included.', 'The document is required in certain circumstances for the particular sequence type, but not all. A list of the sections where content has been provided will be created by the validator for review purposes in content screening. The absence of a required document could lead to the sequence being rejected.'],
            },
        ]
    },
    'ecowassubmissionrules': {
        'columns': [
            {
                'name': 'ecowassubmissionruleid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'submissiontypeid',
                'type': 'bigint',
                'examples': [],
            },
            {
                'name': 'dtdmappingid',
                'type': 'bigint',
                'examples': [],
            },
            {
                'name': 'code',
                'type': 'character varying',
                'examples': ['E', 'NV', 'P', 'W'],
            },
        ]
    },
    'evaluationpath': {
        'columns': [
            {
                'name': 'evaluationpathid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'evaluationpathcode',
                'type': 'character varying',
                'examples': ['eval-path-1', 'eval-path-2', 'eval-path-3', 'eval-path-4', 'eval-path-5'],
            },
            {
                'name': 'evaluationpathvalue',
                'type': 'character varying',
                'examples': ['Abridged Evaluation', 'Full Evaluation', 'Priority', 'Rolling Review', 'Section 21/EUL'],
            },
            {
                'name': 'createddate',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'obsoleteddate',
                'type': 'timestamp without time zone',
                'examples': [],
            },
        ]
    },
    'excipients': {
        'columns': [
            {
                'name': 'excipientid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'productid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'excipientno',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'excipientname',
                'type': 'character varying',
                'examples': ['Carbomer', 'eraggze', 'excipient-01', 'Excipient-01', 'excipient-02'],
            },
            {
                'name': 'createddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'modifiedby',
                'type': 'character varying',
                'examples': ['dyadmin13', 'dyaz', 'dyaz1', 'dyazra', 'wajahat'],
            },
            {
                'name': 'lastupdateddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
        ]
    },
    'imports': {
        'columns': [
            {
                'name': 'importid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'accountid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationnumber',
                'type': 'character varying',
                'examples': ['000000', '000111', '000123', '000456', '000678'],
            },
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'filename',
                'type': 'character varying',
                'examples': ['000111.zip', '000123.zip', '000456.zip', '000678.zip', '000888.zip'],
            },
            {
                'name': 'status',
                'type': 'character varying',
                'examples': ['Application_saved', 'Product_saved', 'Sequence_inprogress', 'Sequence_saved', 'Uploaded'],
            },
            {
                'name': 'importdatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
        ]
    },
    'importsequencesummary': {
        'columns': [
            {
                'name': 'importsequencesummaryid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'importid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequencenumber',
                'type': 'character varying',
                'examples': ['0001', '0002', '0003', '0004', '0012'],
            },
            {
                'name': 'hasindexxml',
                'type': 'boolean',
                'examples': [],
            },
            {
                'name': 'hasregionalxml',
                'type': 'boolean',
                'examples': [],
            },
            {
                'name': 'status',
                'type': 'character varying',
                'examples': ['Errors', 'Published', 'Valid', 'Validating'],
            },
            {
                'name': 'saved',
                'type': 'boolean',
                'examples': [],
            },
        ]
    },
    'indications': {
        'columns': [
            {
                'name': 'indicationid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'principalproductid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'indicationno',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'indicationname',
                'type': 'character varying',
                'examples': ['', 'Bacterial Infection', 'Bodyache', 'Cold Symptoms', 'dddddddd'],
            },
            {
                'name': 'createddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'modifiedby',
                'type': 'character varying',
                'examples': ['dyadmin13', 'dyauthor13', 'dyaz', 'dyaz1', 'dyazra'],
            },
            {
                'name': 'lastupdateddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
        ]
    },
    'placeholders': {
        'columns': [
            {
                'name': 'placeholderid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'templateid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'folderpath',
                'type': 'character varying',
                'examples': ['Templates/100/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.0 Cover Letter/Common', 'Templates/100/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.0 Cover Letter/Ema', 'Templates/100/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.10 Information relating to Paediatrics', 'Templates/100/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.2 Application Form/Ema', 'Templates/100/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.3 Product Information/1.3.1 SmPC, Labelling and Package Leaflet/Annex II/Common/English'],
            },
            {
                'name': 'onedrivefolderid',
                'type': 'character varying',
                'examples': ['01LY4YSOQ22TIWAIX67FDJNDNMJYEG4NZR', '01LY4YSOQ256A5U3YTWRDJYPNNV52LJHGZ', '01LY4YSOQ2DBWGCXOQARGLRLLQS3LJHT4U', '01LY4YSOQ3ED3JDAO4DZBYJZUFIUGQGODQ', '01LY4YSOQ3NFSJ3O4O6BDI5GB4PJYUUA3E'],
            },
            {
                'name': 'placeholdername',
                'type': 'character varying',
                'examples': ['1.12.10 Generic Drug Enforcement Act Statement.pdf', '1.12.11 ANDA Basis for Submission Statement.pdf', '1.12.12 Comparison of Generic Drug and Reference Listed Drug.pdf', '1.12.13 Request for Waiver for in Vivo Studies.pdf', '1.12.14 Environmental Analysis.pdf'],
            },
            {
                'name': 'isactive',
                'type': 'boolean',
                'examples': [],
            },
        ]
    },
    'principalproducts': {
        'columns': [
            {
                'name': 'principalproductid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'accountid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'brandname',
                'type': 'character varying',
                'examples': ['abott', 'abxz', 'Aciloc', 'bngf', 'Brand013'],
            },
            {
                'name': 'principalproductname',
                'type': 'character varying',
                'examples': ['abccc', 'abchsf', 'abott', 'adcvs', 'Azithromycin'],
            },
            {
                'name': 'createddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'modifiedby',
                'type': 'character varying',
                'examples': ['dyadmin13', 'dyauthor13', 'dyaz', 'dyaz1', 'dyazra'],
            },
            {
                'name': 'lastupdateddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'isactive',
                'type': 'boolean',
                'examples': [],
            },
        ]
    },
    'products': {
        'columns': [
            {
                'name': 'productid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'principalproductid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'dosageform',
                'type': 'character varying',
                'examples': ['CAPSULE', 'CREAM', 'Gel', 'INJECTION', 'OINTMENT'],
            },
            {
                'name': 'productmanufacturername',
                'type': 'character varying',
                'examples': ['abott', 'abxzz', 'arott', 'bfdbdfb', 'bhbgh'],
            },
            {
                'name': 'productname',
                'type': 'character varying',
                'examples': ['abcc', 'abott', 'Amoxicillin Capsule', 'Amoxicillin Suspension', 'Azithromycin 250 mg Tablets'],
            },
            {
                'name': 'createddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'modifiedby',
                'type': 'character varying',
                'examples': ['dyadmin13', 'dyauthor13', 'dyaz', 'dyaz1', 'dyazra'],
            },
            {
                'name': 'lastupdateddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
        ]
    },
    'queries': {
        'columns': [
            {
                'name': 'queryid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'assignedtouserid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sourcesequenceid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'createdbyuserid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'targetdatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'status',
                'type': 'character varying',
                'examples': ['inprogress', 'new', 'Resolved'],
            },
            {
                'name': 'title',
                'type': 'character varying',
                'examples': ['87867867', 'bhhjhvhvh', 'European Medicines Agency', 'gfgdf', 'hgjgbhjb'],
            },
            {
                'name': 'description',
                'type': 'text',
                'examples': ['<p><em class="ql-size-large"><u>testghjghjghj</u></em></p>', '<p>hgyjgyghxvsdvs</p>', '<p>kljki</p>', '<p>nbnbjm nm</p>', '<p>n nhvhvghkjhjkhjkhjhk</p>'],
            },
            {
                'name': 'isactive',
                'type': 'boolean',
                'examples': [],
            },
            {
                'name': 'lastupdateddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'accountid',
                'type': 'integer',
                'examples': [],
            },
        ]
    },
    'queryattachments': {
        'columns': [
            {
                'name': 'queryattachmentid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'queryid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'queryattachmenturl',
                'type': 'text',
                'examples': ['https://noohaaspltd-my.sharepoint.com/personal/sadiya_parveen_nooha-asp_com/_layouts/15/download.aspx?UniqueId=06e947f4-8f8b-4a96-b5a7-1e547e70f3d6&Translate=false&tempauth=v1.eyJzaXRlaWQiOiI2NzgzOGI5ZC0yY2UwLTQ2YzEtYmZjYy1kODc3N2U5MWFmNmQiLCJhcHBfZGlzcGxheW5hbWUiOiJkeWF6IiwibmFtZWlkIjoiOGVlN2JlYjMtN2JmYy00YTg3LTlhNTktZjIzMTdmMzYyOTE1QDQ0NWU0YjcwLWUzODYtNGQ3My1iYjMwLTUxOGY1ZTFhYzFhZSIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9ub29oYWFzcGx0ZC1teS5zaGFyZXBvaW50LmNvbUA0NDVlNGI3MC1lMzg2LTRkNzMtYmIzMC01MThmNWUxYWMxYWUiLCJleHAiOiIxNzUzMTE5MjY1In0.CkAKDGVudHJhX2NsYWltcxIwQ0tMTStjTUdFQUFhRm1JMk9HeHRlRUl4ZEVVeWRWOUpPWEpwY21oVFFVRXFBQT09CjIKCmFjdG9yYXBwaWQSJDAwMDAwMDAzLTAwMDAtMDAwMC1jMDAwLTAwMDAwMDAwMDAwMAoKCgRzbmlkEgI2NBILCOyCkdDPn6Q-EAUaCzIwLjIwLjQ0Ljk3KixrZWpqLzFGa0tyMDZRSnZ6Y0lMQ1d3dkFCV3FtampKbmxkOFQ3Ly9BdGtRPTCjATgBQhChtAAvxeAAUHcEZHtVvYmTShBoYXNoZWRwcm9vZnRva2VuegExugE3YWxsc2l0ZXMucmVhZCBhbGxzaXRlcy53cml0ZSBncm91cC53cml0ZSBhbGxmaWxlcy53cml0ZcgBAQ.i5Pplp1646QiSwu8zM1rw4JtHxUohDrGBTzzmPJDlNA&ApiVersion=2.0', 'https://noohaaspltd-my.sharepoint.com/personal/sadiya_parveen_nooha-asp_com/_layouts/15/download.aspx?UniqueId=1a6dae4b-f3e1-46ea-a558-3839a19892ba&Translate=false&tempauth=v1.eyJzaXRlaWQiOiI2NzgzOGI5ZC0yY2UwLTQ2YzEtYmZjYy1kODc3N2U5MWFmNmQiLCJhcHBfZGlzcGxheW5hbWUiOiJkeWF6IiwibmFtZWlkIjoiOGVlN2JlYjMtN2JmYy00YTg3LTlhNTktZjIzMTdmMzYyOTE1QDQ0NWU0YjcwLWUzODYtNGQ3My1iYjMwLTUxOGY1ZTFhYzFhZSIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9ub29oYWFzcGx0ZC1teS5zaGFyZXBvaW50LmNvbUA0NDVlNGI3MC1lMzg2LTRkNzMtYmIzMC01MThmNWUxYWMxYWUiLCJleHAiOiIxNzUxOTYzNzcwIn0.CkAKDGVudHJhX2NsYWltcxIwQ1BhS3M4TUdFQUFhRmpSSFZ6bHVVWGx1Wm10bE1VaEVlRXQ1UVRsUlFVRXFBQT09CjIKCmFjdG9yYXBwaWQSJDAwMDAwMDAzLTAwMDAtMDAwMC1jMDAwLTAwMDAwMDAwMDAwMAoKCgRzbmlkEgI2NBILCObhvMCE_54-EAUaDDIwLjIwLjQ0LjIyNCosMHdyejRpdEQ5UTc3anExNVZ3T1JWK2RKN1BIanBGVGxLcW9xK0FzT2lJWT0wowE4AUIQoa-yOGWAAFBgzDdOvXMvPEoQaGFzaGVkcHJvb2Z0b2tlbnoBMboBN2FsbHNpdGVzLnJlYWQgYWxsc2l0ZXMud3JpdGUgZ3JvdXAud3JpdGUgYWxsZmlsZXMud3JpdGXIAQE.flPkj18oAybwKpQO5dm7q91pd8l9-SWtlQIyJpEhiGM&ApiVersion=2.0', 'https://noohaaspltd-my.sharepoint.com/personal/sadiya_parveen_nooha-asp_com/_layouts/15/download.aspx?UniqueId=e0a2ee05-6a8d-40c9-b1f0-96add49bcdd7&Translate=false&tempauth=v1.eyJzaXRlaWQiOiI2NzgzOGI5ZC0yY2UwLTQ2YzEtYmZjYy1kODc3N2U5MWFmNmQiLCJhcHBfZGlzcGxheW5hbWUiOiJkeWF6IiwibmFtZWlkIjoiOGVlN2JlYjMtN2JmYy00YTg3LTlhNTktZjIzMTdmMzYyOTE1QDQ0NWU0YjcwLWUzODYtNGQ3My1iYjMwLTUxOGY1ZTFhYzFhZSIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9ub29oYWFzcGx0ZC1teS5zaGFyZXBvaW50LmNvbUA0NDVlNGI3MC1lMzg2LTRkNzMtYmIzMC01MThmNWUxYWMxYWUiLCJleHAiOiIxNzUzMTIwODg0In0.CkAKDGVudHJhX2NsYWltcxIwQ0tMTStjTUdFQUFhRm1JMk9HeHRlRUl4ZEVVeWRWOUpPWEpwY21oVFFVRXFBQT09CjIKCmFjdG9yYXBwaWQSJDAwMDAwMDAzLTAwMDAtMDAwMC1jMDAwLTAwMDAwMDAwMDAwMAoKCgRzbmlkEgI2NBILCNr0sJ3IoKQ-EAUaCzIwLjIwLjQ0Ljk3KixUSU9XWGNQSlQ2OVY2bzJlcktEbXdMV2RKR3hGd05BcXAzUjRUUEc1dFhrPTCjATgBQhChtAG6-HAAUHcEZ1lmu4rLShBoYXNoZWRwcm9vZnRva2VuegExugE3YWxsc2l0ZXMucmVhZCBhbGxzaXRlcy53cml0ZSBncm91cC53cml0ZSBhbGxmaWxlcy53cml0ZcgBAQ._DR98m7GEFZpVPeSHBdyflOS9RZogySTWegINY91Djs&ApiVersion=2.0', 'https://noohaaspltd-my.sharepoint.com/personal/shazia_afreen_nooha-asp_com/_layouts/15/download.aspx?UniqueId=0538ca4d-4fed-4dc4-bad1-4494b87bd969&Translate=false&tempauth=v1.eyJzaXRlaWQiOiI5MzhiZjI3NC01MDZkLTQzYmYtOTZmOS1lMWM3NWY2MmRjZDMiLCJhcHBfZGlzcGxheW5hbWUiOiJkeWF6IiwibmFtZWlkIjoiOGVlN2JlYjMtN2JmYy00YTg3LTlhNTktZjIzMTdmMzYyOTE1QDQ0NWU0YjcwLWUzODYtNGQ3My1iYjMwLTUxOGY1ZTFhYzFhZSIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9ub29oYWFzcGx0ZC1teS5zaGFyZXBvaW50LmNvbUA0NDVlNGI3MC1lMzg2LTRkNzMtYmIzMC01MThmNWUxYWMxYWUiLCJleHAiOiIxNzUyNTgxOTc1In0.CkAKDGVudHJhX2NsYWltcxIwQ1BudjJNTUdFQUFhRmtZd1pYTm1UekpIWjBWNVZucE9TMWs1ZEU1eVFVRXFBQT09CjIKCmFjdG9yYXBwaWQSJDAwMDAwMDAzLTAwMDAtMDAwMC1jMDAwLTAwMDAwMDAwMDAwMAoKCgRzbmlkEgI2NBILCODc77Pw5qE-EAUaDDIwLjIwLjQ0LjE2MCosdGNoT3ZYeG5yenkybFdqaXEydDBIQjRqdit1aXo3Qkg4YWlPTlM1WHZIST0wogE4AUIQobH_yXUQAFBgzDXD0DM1yUoQaGFzaGVkcHJvb2Z0b2tlbnoBMboBN2FsbHNpdGVzLnJlYWQgYWxsc2l0ZXMud3JpdGUgZ3JvdXAud3JpdGUgYWxsZmlsZXMud3JpdGXIAQE.9o24e7xct1Yr0sr6ALdDvw2SH-XkIYkUJQgaOihjgLQ&ApiVersion=2.0', 'https://noohaaspltd-my.sharepoint.com/personal/shazia_afreen_nooha-asp_com/_layouts/15/download.aspx?UniqueId=21ac6a09-2e25-4254-9e6d-6413421003fe&Translate=false&tempauth=v1.eyJzaXRlaWQiOiI5MzhiZjI3NC01MDZkLTQzYmYtOTZmOS1lMWM3NWY2MmRjZDMiLCJhcHBfZGlzcGxheW5hbWUiOiJkeWF6IiwibmFtZWlkIjoiOGVlN2JlYjMtN2JmYy00YTg3LTlhNTktZjIzMTdmMzYyOTE1QDQ0NWU0YjcwLWUzODYtNGQ3My1iYjMwLTUxOGY1ZTFhYzFhZSIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9ub29oYWFzcGx0ZC1teS5zaGFyZXBvaW50LmNvbUA0NDVlNGI3MC1lMzg2LTRkNzMtYmIzMC01MThmNWUxYWMxYWUiLCJleHAiOiIxNzUwMTgzNjE4In0.CjIKCmFjdG9yYXBwaWQSJDAwMDAwMDAzLTAwMDAtMDAwMC1jMDAwLTAwMDAwMDAwMDAwMAoKCgRzbmlkEgI2NBILCI6fuuzs8pY-EAUaDTIwLjE5MC4xNzQuNDMqLDFTSjAwcG5yb0ovd0VkdUVCL1F2eWdXVTNLQnpWR3hPa0lGMEo1Skh0ZVk9MKIBOAFCEKGpEIjv8ABQTQVkPGpnF6xKEGhhc2hlZHByb29mdG9rZW56ATG6ATdhbGxzaXRlcy5yZWFkIGFsbHNpdGVzLndyaXRlIGdyb3VwLndyaXRlIGFsbGZpbGVzLndyaXRlyAEB.J06AmTRzjgBmY5dtP0G2mBRuSjQ0hw6KH84Ukkhrq_A&ApiVersion=2.0'],
            },
        ]
    },
    'queryresponseattachments': {
        'columns': [
            {
                'name': 'queryresponseattachmentid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'queryresponseid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'responseattachmenturl',
                'type': 'text',
                'examples': ['https://noohaaspltd-my.sharepoint.com/personal/sadiya_parveen_nooha-asp_com/_layouts/15/download.aspx?UniqueId=47ce6ce6-d810-475b-bc09-f6a9e6a5f5c9&Translate=false&tempauth=v1.eyJzaXRlaWQiOiI2NzgzOGI5ZC0yY2UwLTQ2YzEtYmZjYy1kODc3N2U5MWFmNmQiLCJhcHBfZGlzcGxheW5hbWUiOiJkeWF6IiwibmFtZWlkIjoiOGVlN2JlYjMtN2JmYy00YTg3LTlhNTktZjIzMTdmMzYyOTE1QDQ0NWU0YjcwLWUzODYtNGQ3My1iYjMwLTUxOGY1ZTFhYzFhZSIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9ub29oYWFzcGx0ZC1teS5zaGFyZXBvaW50LmNvbUA0NDVlNGI3MC1lMzg2LTRkNzMtYmIzMC01MThmNWUxYWMxYWUiLCJleHAiOiIxNzUyNTEzNzk2In0.CkAKDGVudHJhX2NsYWltcxIwQ0pqUTFNTUdFQUFhRmt0RWRUWm5NWFpNUld0TE5tVXpaM2hGTUhsdFFVRXFBQT09CjIKCmFjdG9yYXBwaWQSJDAwMDAwMDAzLTAwMDAtMDAwMC1jMDAwLTAwMDAwMDAwMDAwMAoKCgRzbmlkEgI2NBILCNbKydCYv6E-EAUaDDIwLjIwLjQ0LjIyNCosZW4wcEVuRWpWWVVMZG4rYVl0TjRCNlJWYmFNSGgvaXdSYmNQZWw5V1lYZz0wowE4AUIQobG-w_fQAFBgzD21Nnaj7EoQaGFzaGVkcHJvb2Z0b2tlbnoBMboBN2FsbHNpdGVzLnJlYWQgYWxsc2l0ZXMud3JpdGUgZ3JvdXAud3JpdGUgYWxsZmlsZXMud3JpdGXIAQE.U-eMEq8Kq4Rdb0tRGfJy5vVE4PuCEFL8MbPzNdfT8Vw&ApiVersion=2.0', 'https://noohaaspltd-my.sharepoint.com/personal/sadiya_parveen_nooha-asp_com/_layouts/15/download.aspx?UniqueId=5af8c57f-6de9-48dc-a783-f94980258bac&Translate=false&tempauth=v1.eyJzaXRlaWQiOiI2NzgzOGI5ZC0yY2UwLTQ2YzEtYmZjYy1kODc3N2U5MWFmNmQiLCJhcHBfZGlzcGxheW5hbWUiOiJkeWF6IiwibmFtZWlkIjoiOGVlN2JlYjMtN2JmYy00YTg3LTlhNTktZjIzMTdmMzYyOTE1QDQ0NWU0YjcwLWUzODYtNGQ3My1iYjMwLTUxOGY1ZTFhYzFhZSIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9ub29oYWFzcGx0ZC1teS5zaGFyZXBvaW50LmNvbUA0NDVlNGI3MC1lMzg2LTRkNzMtYmIzMC01MThmNWUxYWMxYWUiLCJleHAiOiIxNzUyNTEzNzk1In0.CkAKDGVudHJhX2NsYWltcxIwQ0pqUTFNTUdFQUFhRmt0RWRUWm5NWFpNUld0TE5tVXpaM2hGTUhsdFFVRXFBQT09CjIKCmFjdG9yYXBwaWQSJDAwMDAwMDAzLTAwMDAtMDAwMC1jMDAwLTAwMDAwMDAwMDAwMAoKCgRzbmlkEgI2NBILCOrEoMmYv6E-EAUaDDIwLjIwLjQ0LjIyNCosTWNhY1ZxekRlejdhQTlmUHY2WDIrWWM3UVhVM1R3bFE2cTBFVUZzTStFcz0wowE4AUIQobG-w9hwAFBgzDSeiKPzhUoQaGFzaGVkcHJvb2Z0b2tlbnoBMboBN2FsbHNpdGVzLnJlYWQgYWxsc2l0ZXMud3JpdGUgZ3JvdXAud3JpdGUgYWxsZmlsZXMud3JpdGXIAQE.jmrviG9JTWT2CyRV4G2cJI3LQJb7134Lfr46Gtuuhig&ApiVersion=2.0', 'https://noohaaspltd-my.sharepoint.com/personal/sadiya_parveen_nooha-asp_com/_layouts/15/download.aspx?UniqueId=97d2bbee-7daf-41ba-bb5a-745196ce987d&Translate=false&tempauth=v1.eyJzaXRlaWQiOiI2NzgzOGI5ZC0yY2UwLTQ2YzEtYmZjYy1kODc3N2U5MWFmNmQiLCJhcHBfZGlzcGxheW5hbWUiOiJkeWF6IiwibmFtZWlkIjoiOGVlN2JlYjMtN2JmYy00YTg3LTlhNTktZjIzMTdmMzYyOTE1QDQ0NWU0YjcwLWUzODYtNGQ3My1iYjMwLTUxOGY1ZTFhYzFhZSIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9ub29oYWFzcGx0ZC1teS5zaGFyZXBvaW50LmNvbUA0NDVlNGI3MC1lMzg2LTRkNzMtYmIzMC01MThmNWUxYWMxYWUiLCJleHAiOiIxNzUyNTEzNzk3In0.CkAKDGVudHJhX2NsYWltcxIwQ0pqUTFNTUdFQUFhRmt0RWRUWm5NWFpNUld0TE5tVXpaM2hGTUhsdFFVRXFBQT09CjIKCmFjdG9yYXBwaWQSJDAwMDAwMDAzLTAwMDAtMDAwMC1jMDAwLTAwMDAwMDAwMDAwMAoKCgRzbmlkEgI2NBILCIDGt9uYv6E-EAUaDDIwLjIwLjQ0LjIyNCosU3l3eENGUU9OOVE4OWtIaFRIQ3hzdHlyTjR5R1phS1c5WlU2WExsUDJtVT0wowE4AUIQobG-xCtwAFBgzD9fpVuBjEoQaGFzaGVkcHJvb2Z0b2tlbnoBMboBN2FsbHNpdGVzLnJlYWQgYWxsc2l0ZXMud3JpdGUgZ3JvdXAud3JpdGUgYWxsZmlsZXMud3JpdGXIAQE.IKkOVelZM4I238eF53AwKFGj9-Ct1Se9GhGxHPsqKh0&ApiVersion=2.0', 'https://noohaaspltd-my.sharepoint.com/personal/sadiya_parveen_nooha-asp_com/_layouts/15/download.aspx?UniqueId=9bc397ce-4ee0-4d4a-8a21-acdde25051fb&Translate=false&tempauth=v1.eyJzaXRlaWQiOiI2NzgzOGI5ZC0yY2UwLTQ2YzEtYmZjYy1kODc3N2U5MWFmNmQiLCJhcHBfZGlzcGxheW5hbWUiOiJkeWF6IiwibmFtZWlkIjoiOGVlN2JlYjMtN2JmYy00YTg3LTlhNTktZjIzMTdmMzYyOTE1QDQ0NWU0YjcwLWUzODYtNGQ3My1iYjMwLTUxOGY1ZTFhYzFhZSIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9ub29oYWFzcGx0ZC1teS5zaGFyZXBvaW50LmNvbUA0NDVlNGI3MC1lMzg2LTRkNzMtYmIzMC01MThmNWUxYWMxYWUiLCJleHAiOiIxNzUyNTEzNzk0In0.CkAKDGVudHJhX2NsYWltcxIwQ0pqUTFNTUdFQUFhRmt0RWRUWm5NWFpNUld0TE5tVXpaM2hGTUhsdFFVRXFBQT09CjIKCmFjdG9yYXBwaWQSJDAwMDAwMDAzLTAwMDAtMDAwMC1jMDAwLTAwMDAwMDAwMDAwMAoKCgRzbmlkEgI2NBILCPTyn8WYv6E-EAUaDDIwLjIwLjQ0LjIyNCosSzZEc3Bmd0dRbVpIbnYvaVNrR09aZ014b1pQMENOb3Rrd2NUOFhTc21tVT0wowE4AUIQobG-w6yQAFBgzDITfLivdEoQaGFzaGVkcHJvb2Z0b2tlbnoBMboBN2FsbHNpdGVzLnJlYWQgYWxsc2l0ZXMud3JpdGUgZ3JvdXAud3JpdGUgYWxsZmlsZXMud3JpdGXIAQE.Qa-orrAyBNyfJFH9tFbLbDcRj2beIRgUG_9exN-5HCo&ApiVersion=2.0', 'https://noohaaspltd-my.sharepoint.com/personal/shazia_afreen_nooha-asp_com/_layouts/15/download.aspx?UniqueId=0c6c75dd-5c36-4a72-b3fa-5e269070801a&Translate=false&tempauth=v1.eyJzaXRlaWQiOiI5MzhiZjI3NC01MDZkLTQzYmYtOTZmOS1lMWM3NWY2MmRjZDMiLCJhcHBfZGlzcGxheW5hbWUiOiJkeWF6IiwibmFtZWlkIjoiOGVlN2JlYjMtN2JmYy00YTg3LTlhNTktZjIzMTdmMzYyOTE1QDQ0NWU0YjcwLWUzODYtNGQ3My1iYjMwLTUxOGY1ZTFhYzFhZSIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9ub29oYWFzcGx0ZC1teS5zaGFyZXBvaW50LmNvbUA0NDVlNGI3MC1lMzg2LTRkNzMtYmIzMC01MThmNWUxYWMxYWUiLCJleHAiOiIxNzUyNTc4NTkzIn0.CkAKDGVudHJhX2NsYWltcxIwQ1AvSzJNTUdFQUFhRmxCTlIwcHdja05FUzBWdFduRXdVaTFaT0UxblFVRXFBQT09CjIKCmFjdG9yYXBwaWQSJDAwMDAwMDAzLTAwMDAtMDAwMC1jMDAwLTAwMDAwMDAwMDAwMAoKCgRzbmlkEgI2NBILCP7Y3rD05KE-EAUaDDIwLjIwLjQ0LjE2MCosK05Xayt6Z3RJcjBqUzVxZUJqNzNOK0tsS3phSi9MT2g1Y3laMDBTWHhSST0wogE4AUIQobH8j4gwAFB3o_Lmknf61EoQaGFzaGVkcHJvb2Z0b2tlbnoBMboBN2FsbHNpdGVzLnJlYWQgYWxsc2l0ZXMud3JpdGUgZ3JvdXAud3JpdGUgYWxsZmlsZXMud3JpdGXIAQE.Zcouny5rCYvNTwRlnEU2iQ5OwS4mWCEZeeprZ1EaFv0&ApiVersion=2.0'],
            },
        ]
    },
    'queryresponses': {
        'columns': [
            {
                'name': 'queryresponseid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'queryid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'createddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'title',
                'type': 'character varying',
                'examples': ['cndnjjdgjfgn', 'gfgjfgjf', 'hjghj', 'jgjfgjgf', 'Query response to USFDA query 16'],
            },
            {
                'name': 'description',
                'type': 'text',
                'examples': ['ghjghghvhv', '<p>dfhdjndnjfgn</p>', '<p>fdnfgmgh,</p>', '<p>hjj</p>', '<p>ngndgjfgm</p>'],
            },
        ]
    },
    'recipients': {
        'columns': [
            {
                'name': 'recipientid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'recipientcode',
                'type': 'character varying',
                'examples': ['', 'bj', 'ci', 'cv', 'gm'],
            },
            {
                'name': 'leadnmracode',
                'type': 'character varying',
                'examples': ['', 'bj', 'ci', 'gh', 'gm'],
            },
        ]
    },
    'regions': {
        'columns': [
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'region',
                'type': 'character varying',
                'examples': ['ECOWAS', 'EU', 'GCC', 'ROW', 'SAHPRA'],
            },
        ]
    },
    'sahprasubmissionrules': {
        'columns': [
            {
                'name': 'sahprasubmissionruleid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'submissiontypeid',
                'type': 'bigint',
                'examples': [],
            },
            {
                'name': 'dtdmappingid',
                'type': 'bigint',
                'examples': [],
            },
            {
                'name': 'code',
                'type': 'character varying',
                'examples': ['E', 'NV', 'NYD', 'P', 'W'],
            },
        ]
    },
    'sequencefileapprover': {
        'columns': [
            {
                'name': 'sequencefileapproverid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'assignoruserid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequencefileid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequencefileapproveruserid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'enddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'priority',
                'type': 'character varying',
                'examples': [],
            },
        ]
    },
    'sequencefilereviewer': {
        'columns': [
            {
                'name': 'sequencefilereviewerid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequencefileid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'assignoruserid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequencerevieweruserid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'enddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'priority',
                'type': 'character varying',
                'examples': [],
            },
        ]
    },
    'sequencefiles': {
        'columns': [
            {
                'name': 'sequencefileid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequenceid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'templatefileid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'filename',
                'type': 'character varying',
                'examples': ['00-02-test.docx', '00-02-test.pdf', '00-03-test99087uuhhsbnniigig.docx', '00-03-test99087uuhhsbnniigig.pdf', '00-04-testword.docx'],
            },
            {
                'name': 'filepath',
                'type': 'character varying',
                'examples': ['Applications/Published/000111/0002/util/dtd/ich-ectd-3-2.dtd', 'Applications/Published/000111/0002/util/style/ectd-2-0.xsl', 'Applications/Published/009888/0002/util/dtd/ich-ectd-3-2.dtd', 'Applications/Published/009888/0002/util/style/ectd-2-0.xsl', 'Applications/Published/0101011/0003/index-md5.txt'],
            },
            {
                'name': 'checksum',
                'type': 'character varying',
                'examples': ['0104ca4826a0a912eb340a3a5fb8cef5', '0c30fcf4ecbbdc8483f331bed2931d16', '101797c35d7e56370e476c32d5274efe', '1023c50933ccdde50a3e11dd969d871a', '104a7ea4bb985cf98e8f6ac0bea23807'],
            },
            {
                'name': 'status',
                'type': 'character varying',
                'examples': ['0'],
            },
            {
                'name': 'operation',
                'type': 'character varying',
                'examples': ['new'],
            },
            {
                'name': 'leaftitle',
                'type': 'character varying',
                'examples': ['00-02-test.docx', '00-02-test.pdf', '00-03-test99087uuhhsbnniigig.docx', '00-03-test99087uuhhsbnniigig.pdf', '00-04-testword.docx'],
            },
            {
                'name': 'modifiedfilepath',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'href',
                'type': 'character varying',
                'examples': ['Applications/Published/EU23456/0000/m1/eu/10-cover/32p1-desc-comp/32p1-description-n-composition.pdf', 'Applications/Published/EU23456/0000/m1/eu/10-cover/emea-cover.pdf', 'Applications/Published/EU23456/0000/m1/eu/10-cover/New Microsoft Word Document.docx', 'Applications/Published/EU23456/0000/m1/eu/10-cover/Validation Error Report -0003.pdf', 'Applications/Published/EU23456/0000/m1/eu/110-paediatrics/clinicaltrials.pdf'],
            },
            {
                'name': 'createddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'origin',
                'type': 'character varying',
                'examples': ['file-sample_100kB.docx', 'Validation Error Report -214 (2).pdf'],
            },
        ]
    },
    'sequenceproducts': {
        'columns': [
            {
                'name': 'sequenceid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'productid',
                'type': 'integer',
                'examples': [],
            },
        ]
    },
    'sequences': {
        'columns': [
            {
                'name': 'sequenceid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequencenumber',
                'type': 'character varying',
                'examples': ['0000', '0001', '0002', '0003', '0004'],
            },
            {
                'name': 'accountid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'userid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'templateid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'submissiontypeid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'submissionsubtypesid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequencecreatoruserid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequencerevieweruserid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequenceapproveruserid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'submissiontargetagentuserid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'actualsubmissionagentuserid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'submissionid',
                'type': 'character varying',
                'examples': ['', '0000', '0001', '0002', '0004'],
            },
            {
                'name': 'submissiondescription',
                'type': 'character varying',
                'examples': ['', 'aaa', 'aaaa', 'ababab', 'abcabca'],
            },
            {
                'name': 'isactive',
                'type': 'boolean',
                'examples': [],
            },
            {
                'name': 'status',
                'type': 'character varying',
                'examples': ['COMPILED', 'COMPILE_ERRORS', 'DELETED', 'DRAFT', 'ERRORS'],
            },
            {
                'name': 'submissiontargetdatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'reviewertargetdatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'revieweddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'approveddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'createddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'approvertargetdatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'creatortargetdatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'priority',
                'type': 'character varying',
                'examples': ['high'],
            },
            {
                'name': 'actualsubmissiondatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'lastupdateddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'modifiedby',
                'type': 'character varying',
                'examples': ['adarsh', 'dyadmin13', 'dyauthor13', 'dyaz', 'dyaz1'],
            },
            {
                'name': 'onedriveapplicationfolderid',
                'type': 'character varying',
                'examples': ['013WTN3O3POQMSDF7JTVAJDIUFUBTGXTRW', '01LY4YSOQDVOTHGEWUQFCIZWF7QN76GA7C', '01LY4YSOQMEVZXH6LSU5CIVGCWNUMOSWZV', '01LY4YSORIK2U3UUPRUJGIPNWNIXBCWPVH', '01LY4YSORINIEWIQYHSBAZQORQKSH5WUQS'],
            },
            {
                'name': 'regionaldtd',
                'type': 'character varying',
                'examples': ['1.0', '1.1', '3.1', '3.3'],
            },
            {
                'name': 'ichdtd',
                'type': 'character varying',
                'examples': ['3.2'],
            },
            {
                'name': 'rowsubmissiontype',
                'type': 'character varying',
                'examples': ['ctd', 'fgf', 'init', 'Initial', 'NDA-APP'],
            },
            {
                'name': 'rowsubmissionsubtype',
                'type': 'character varying',
                'examples': ['Amendment', 'chemical', 'dfds', 'dsgfs', 'dthdd'],
            },
            {
                'name': 'principalproductid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'tocheaderleft',
                'type': 'character varying',
                'examples': ['', 'abccc', 'acet', 'bdfgdfgb', 'header'],
            },
            {
                'name': 'tocheadercenter',
                'type': 'character varying',
                'examples': ['', '661121', 'centerh', 'CenterHeader', 'cip'],
            },
            {
                'name': 'tocheaderright',
                'type': 'character varying',
                'examples': ['', 'fdgdfgdf', 'headerl', 'rightH', 'RightHeader'],
            },
            {
                'name': 'tocfooterleft',
                'type': 'character varying',
                'examples': ['', 'acetoe', 'dfgdfgdf', 'footer', 'leftF'],
            },
            {
                'name': 'tocfootercenter',
                'type': 'character varying',
                'examples': ['', '661121', 'centerF', 'CenterFooter', 'cipla'],
            },
            {
                'name': 'tocfooterright',
                'type': 'character varying',
                'examples': ['', 'footerl', 'gdfgdfg', 'rightF', 'RightFooter'],
            },
            {
                'name': 'submissionnumber',
                'type': 'character varying',
                'examples': ['', '01910', '65699'],
            },
            {
                'name': 'sequencedate',
                'type': 'date',
                'examples': [],
            },
            {
                'name': 'apimfnumber',
                'type': 'character varying',
                'examples': ['', '0200020', '5432'],
            },
            {
                'name': 'pmfnumber',
                'type': 'character varying',
                'examples': ['', '111100000', '2345', 'sh2h22j'],
            },
            {
                'name': 'vamfnumber',
                'type': 'character varying',
                'examples': ['', '3993383hd', '5432'],
            },
            {
                'name': 'smfnumber',
                'type': 'character varying',
                'examples': ['', '2345', '282992s'],
            },
            {
                'name': 'submissionleadid',
                'type': 'bigint',
                'examples': [],
            },
            {
                'name': 'evaluationpathid',
                'type': 'bigint',
                'examples': [],
            },
        ]
    },
    'sequencetasks': {
        'columns': [
            {
                'name': 'id',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequenceid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationnumber',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'creator',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'reviewer',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'approver',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'creatortargetdate',
                'type': 'timestamp with time zone',
                'examples': [],
            },
            {
                'name': 'reviewertargetdate',
                'type': 'timestamp with time zone',
                'examples': [],
            },
            {
                'name': 'approvertargetdate',
                'type': 'timestamp with time zone',
                'examples': [],
            },
            {
                'name': 'submissiontargetdate',
                'type': 'timestamp with time zone',
                'examples': [],
            },
            {
                'name': 'prioritydate',
                'type': 'timestamp with time zone',
                'examples': [],
            },
            {
                'name': 'status',
                'type': 'character varying',
                'examples': [],
            },
        ]
    },
    'sequencevariable': {
        'columns': [
            {
                'name': 'sequencevariableid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequencefileid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'templatefileid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'variablename',
                'type': 'character varying',
                'examples': ['abbbss', 'ciplaa', 'cipppa', 'citrin', 'dollo'],
            },
            {
                'name': 'filepath',
                'type': 'character varying',
                'examples': ['Applications/Source/9811544/0006/Module 1 Administrative Information and Prescribing Information/1.A Additional Data/administrative-information.pdf', 'Applications/Source/9811544/0007/Module 1 Administrative Information and Prescribing Information/1.A Additional Data/sample.pdf'],
            },
        ]
    },
    'signature': {
        'columns': [
            {
                'name': 'signatureid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'objectstorageurl',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'objecttoken',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'username',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'emailid',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'documentname',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'fileid',
                'type': 'character varying',
                'examples': [],
            },
            {
                'name': 'timestamp',
                'type': 'character varying',
                'examples': [],
            },
        ]
    },
    'submissionlead': {
        'columns': [
            {
                'name': 'submissionleadid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'submissionleadcode',
                'type': 'character varying',
                'examples': ['sub-lead-1', 'sub-lead-2', 'sub-lead-3', 'sub-lead-4', 'sub-lead-5'],
            },
            {
                'name': 'submissionleadvalue',
                'type': 'character varying',
                'examples': ['Biologicals', 'Complementary', 'Master Files', 'Medical Devices', 'Orthodox'],
            },
            {
                'name': 'createddate',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'obsoleteddate',
                'type': 'timestamp without time zone',
                'examples': [],
            },
        ]
    },
    'submissionsubtypes': {
        'columns': [
            {
                'name': 'submissionsubtypesid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'submissionsubtypecode',
                'type': 'character varying',
                'examples': ['additional-info', 'closing', 'consolidating', 'correction', 'corrigendum'],
            },
            {
                'name': 'submissionsubtypevalue',
                'type': 'character varying',
                'examples': ['Additional Info', 'Amendment', 'Application', 'Biological', 'Blood Products'],
            },
            {
                'name': 'createddate',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'obsoleteddate',
                'type': 'timestamp without time zone',
                'examples': [],
            },
        ]
    },
    'submissiontypes': {
        'columns': [
            {
                'name': 'submissiontypeid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'submissiontypecode',
                'type': 'character varying',
                'examples': ['annual-reassessment', 'article-58', 'asmf', 'cep', 'clin-data-pub-fv'],
            },
            {
                'name': 'submissiontypevalue',
                'type': 'character varying',
                'examples': ['Annual Reassessment', 'Annual Report', 'Application withdrawal', 'Application Withdrawal/Cancellation', 'Article 58'],
            },
            {
                'name': 'createddate',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'obsoleteddate',
                'type': 'timestamp without time zone',
                'examples': [],
            },
        ]
    },
    'substances': {
        'columns': [
            {
                'name': 'substancesid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'principalproductid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'substanceno',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'substancename',
                'type': 'character varying',
                'examples': ['', 'abbbss', 'abcc', 'abott', 'acetone'],
            },
            {
                'name': 'substancemanufacturername',
                'type': 'character varying',
                'examples': ['', '3essssc', 'ABC Chemicals', 'abott', 'abxz'],
            },
            {
                'name': 'createddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'modifiedby',
                'type': 'character varying',
                'examples': ['dyadmin13', 'dyauthor13', 'dyaz', 'dyaz1', 'dyazra'],
            },
            {
                'name': 'lastupdateddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
        ]
    },
    'technicalerrors': {
        'columns': [
            {
                'name': 'technicalerrorid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequenceid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'errorcode',
                'type': 'character varying',
                'examples': ['TR-01', 'TR-03', 'TR-04'],
            },
            {
                'name': 'errordescription',
                'type': 'character varying',
                'examples': ["Lowest-level node 'admin/applicant-info/applicant-contacts/applicant-contact/applicant-contact-name/applicant-contact-name' in file 'Applications/Published/110725/0001/m1/us/us-regional.xml' does not contain a <leaf>.", "Lowest-level node 'admin/applicant-info/applicant-contacts/applicant-contact/applicant-contact-name/applicant-contact-name' in file 'Applications/Published/216344/0002/m1/us/us-regional.xml' does not contain a <leaf>.", "Lowest-level node 'admin/applicant-info/applicant-contacts/applicant-contact/applicant-contact-name/applicant-contact-name' in file 'Applications/Published/291976/0002/m1/us/us-regional.xml' does not contain a <leaf>.", "Lowest-level node 'admin/applicant-info/applicant-contacts/applicant-contact/applicant-contact-name/applicant-contact-name' in file 'Applications/Published/993344/0002/m1/us/us-regional.xml' does not contain a <leaf>.", "Lowest-level node 'admin/applicant-info/applicant-contacts/applicant-contact/emails/email/email' in file 'Applications/Published/110725/0001/m1/us/us-regional.xml' does not contain a <leaf>."],
            },
            {
                'name': 'location',
                'type': 'character varying',
                'examples': ['00-02-test.docx', '000888/0001', '040507/0001', '0911011/0008', '110099/0003'],
            },
        ]
    },
    'telephonetypes': {
        'columns': [
            {
                'name': 'telephonetypeid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'telephonetypecode',
                'type': 'character varying',
                'examples': ['fdatnt1', 'fdatnt2', 'fdatnt3'],
            },
            {
                'name': 'telephonetypevalue',
                'type': 'character varying',
                'examples': ['Business Telephone Number', 'Fax Telephone Number', 'Mobile Telephone Number'],
            },
        ]
    },
    'templatefiles': {
        'columns': [
            {
                'name': 'templatefileid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'placeholderid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'templateid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'filename',
                'type': 'character varying',
                'examples': ['00-02-test.docx', '00-03-test99087uuhhsbnniigig.docx', '00-04-testword.docx', '001-2-cover-letter.docx', '01-testword-%^&(9009977e677899q00).doc'],
            },
            {
                'name': 'createddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'filepath',
                'type': 'character varying',
                'examples': ['Templates/101/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.0 Cover Letter/Common/Validation Error Report -0003.pdf', 'Templates/101/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.2 Application Form/Ema/Validation Error Report -0003.pdf', 'Templates/101/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.3 Product Information/1.3.2 Mock-up/Common/Validation Error Report -0003.pdf', 'Templates/101/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.3 Product Information/1.3.2 Mock-up/Ema/Validation Error Report -0003.pdf', 'Templates/104/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.1 Forms/00-02-test.docx'],
            },
            {
                'name': 'checksum',
                'type': 'character varying',
                'examples': ['0c30fcf4ecbbdc8483f331bed2931d16', '101797c35d7e56370e476c32d5274efe', '10e9a1bbed38abc2ec980ebab7451b80', '1162c40392d9889cf4164d409c76dcf7', '12b40a976356772ebc0e5e71dc09e86a'],
            },
        ]
    },
    'templates': {
        'columns': [
            {
                'name': 'templateid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'accountid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'applicationtypeid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'submissiontypeid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'submissionsubtypesid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'name',
                'type': 'character varying',
                'examples': ['0001', '01-GCC-AC013', '01-GCC-AC013 - Copy', '02-GCC-AC013', '03-GCC-AC013'],
            },
            {
                'name': 'structuretype',
                'type': 'character varying',
                'examples': ['basic', 'Basic Structure', 'Skeleton'],
            },
            {
                'name': 'createddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'modifiedby',
                'type': 'character varying',
                'examples': ['acme', 'dyadmin13', 'dyauthor13', 'dyaz', 'dyaz1'],
            },
            {
                'name': 'islocked',
                'type': 'boolean',
                'examples': [],
            },
            {
                'name': 'isactive',
                'type': 'boolean',
                'examples': [],
            },
            {
                'name': 'onedrivefolderid',
                'type': 'character varying',
                'examples': ['013WTN3O42CVLQVQLB5RCKLC627ZDYFHN6', '013WTN3O4PKSD4NNWREVHJDDF632TVWLFX', '01ERXZXF437YOK75F7YRG2OTLNMGONFLIO', '01LY4YSOQ3LWT3WV5TFRD2SAADQP3XH7NZ', '01LY4YSOQIBJRI2G5BCZFYNW7ETW4XSCFJ'],
            },
            {
                'name': 'submissionformat',
                'type': 'character varying',
                'examples': ['ctd', 'ectd'],
            },
            {
                'name': 'lastupdateddatetime',
                'type': 'timestamp without time zone',
                'examples': [],
            },
            {
                'name': 'rowapplicationtype',
                'type': 'character varying',
                'examples': ['app1', 'initial', 'NDA-APP', 'Rest of the World', 'ROW1'],
            },
            {
                'name': 'rowsubmissiontype',
                'type': 'character varying',
                'examples': ['0001', 'asmf', 'init', 'Original-Submission', 'ST1'],
            },
            {
                'name': 'rowsubmissionsubtype',
                'type': 'character varying',
                'examples': ['87867867', 'additional-info', 'Amendment-Subtype', 'ausbqq', 'init'],
            },
        ]
    },
    'templatevariable': {
        'columns': [
            {
                'name': 'templatevariableid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'fileid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'variablename',
                'type': 'character varying',
                'examples': ['Product Manufacturer', 'Product Name', 'Substance Manufacturer', 'Substance Name'],
            },
            {
                'name': 'filepath',
                'type': 'character varying',
                'examples': ['Templates/116/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.A Additional Data/administrative-information.pdf', 'Templates/117/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.A Additional Data/1-0-cover-letter-esigned.pdf', 'Templates/117/ApplicationId/SequenceId/Module 3 Quality/3.2 Body of Data/3.2.A Appendices/1-0-cover-letter-esigned.pdf', 'Templates/120/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.A Additional Data/sample.pdf', 'Templates/128/ApplicationId/SequenceId/Module 1 Administrative Information and Prescribing Information/1.A Additional Data/1.A.1 Country Specific Data/Spring Start Here.pdf'],
            },
        ]
    },
    'utilfiles': {
        'columns': [
            {
                'name': 'utilfileid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'filename',
                'type': 'character varying',
                'examples': ['ectd-2-0.xsl', 'eu-envelope.mod', 'eu-leaf.mod', 'eu-regional.dtd', 'eu-regional.xsl'],
            },
            {
                'name': 'version',
                'type': 'character varying',
                'examples': ['1.0', '1.1', '1.2', '1.4', '2.0'],
            },
            {
                'name': 'checksum',
                'type': 'character varying',
                'examples': ['0e089da2bc79ddec16c8496e1644d558', '10b9d3e7bd47343d832c0ea317d1e7d5', '1d6f631cc6b6357f0f4fe378e5f79a27', '23b854174e61c68044b9f53c0009af95', '3a07a202455e954a2eb203c5bb443f77'],
            },
            {
                'name': 'effectivedatetime',
                'type': 'timestamp with time zone',
                'examples': [],
            },
            {
                'name': 'lastupdateddatetime',
                'type': 'timestamp with time zone',
                'examples': [],
            },
        ]
    },
    'validationcritiria': {
        'columns': [
            {
                'name': 'validationcritiriaid',
                'type': 'bigint',
                'examples': [],
            },
            {
                'name': 'regionid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'version',
                'type': 'character varying',
                'examples': ['1.0', '1.4', '3.1.1', '4.4', '8.0'],
            },
        ]
    },
    'validationerrors': {
        'columns': [
            {
                'name': 'validationerrorid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'sequenceid',
                'type': 'integer',
                'examples': [],
            },
            {
                'name': 'severity',
                'type': 'character varying',
                'examples': ['Best practice', 'Best Practice', 'Error', 'Fail', 'Fail,Attribute value "1005" of type ID must be an NCName when namespaces are enabled.'],
            },
            {
                'name': 'filename',
                'type': 'character varying',
                'examples': ['', '00-02-test.pdf', '00-03-test99087uuhhsbnniigig.pdf', '0004', '00-04-testword.pdf'],
            },
            {
                'name': 'location',
                'type': 'character varying',
                'examples': ['', '0000', '0001', '0001/m1/za', '0007'],
            },
            {
                'name': 'category',
                'type': 'character varying',
                'examples': ['1 ICH DTD', 'Bookmarks', 'Content', 'dtd', 'ectd-2-0.xsl'],
            },
            {
                'name': 'errorcode',
                'type': 'character varying',
                'examples': ['0', '10.1', '10.2', '10.3', '10.4'],
            },
            {
                'name': 'errordescription',
                'type': 'character varying',
                'examples': ['1.0.1 Cover Letter file missing', '1.0.1 Cover Letter file missing. The document is required in the sequence being submitted. If no document is present, it will lead to a validation error and the sequence being rejected.', '1.0.1 Letter of Application file missing. The document is required in the sequence being submitted. If no document is present, it will lead to a validation error and the sequence being rejected.', '1.0.1 Letter of Application must exist', '1.0.2 General Note to Reviewer file missing. The document is required in the sequence being submitted. If no document is present, it will lead to a validation error and the sequence being rejected.'],
            },
            {
                'name': 'comment',
                'type': 'character varying',
                'examples': ['0 bookmark with unknown or unsupported actions', '0 Hyperlinks and Bookmarks within the same sequence must have a valid target', "0 hyperlinks missing 'Inherit Zoom' setting", '0 hyperlinks with missing or broken URI', '0 hyperlinks with unknown or unsupported actions'],
            },
        ]
    },
}

# Table names
TABLE_NAMES = ['applicationcontactdetails', 'applicationcountries', 'applicationcrossreferences', 'applications', 'applicationtypes', 'auditlogs', 'contacttypes', 'countries', 'databasechangelog', 'databasechangeloglock', 'documentmatrix', 'documenttasks', 'dtdmapping', 'ecowasdocumentmatrix', 'ecowassubmissionrules', 'evaluationpath', 'excipients', 'imports', 'importsequencesummary', 'indications', 'placeholders', 'principalproducts', 'products', 'queries', 'queryattachments', 'queryresponseattachments', 'queryresponses', 'recipients', 'regions', 'sahprasubmissionrules', 'sequencefileapprover', 'sequencefilereviewer', 'sequencefiles', 'sequenceproducts', 'sequences', 'sequencetasks', 'sequencevariable', 'signature', 'submissionlead', 'submissionsubtypes', 'submissiontypes', 'substances', 'technicalerrors', 'telephonetypes', 'templatefiles', 'templates', 'templatevariable', 'utilfiles', 'validationcritiria', 'validationerrors']

# Column alias mappings
COLUMN_ALIASES = {
    'email': ['emailid', 'email', 'mailid'],
    'name': ['name', 'applicantname', 'contactname', 'productname'],
    'phone': ['telephonumber', 'phonenumber', 'mobile'],
    'address': ['country', 'region', 'location'],
}
