
db.createCollection( 'projects', {validator: {$jsonSchema: {bsonType: 'object',required: [         'owner',          'post_date',          'username',          'brief',          'closing_date',          'title',          'user',          'category'],properties: {owner: {bsonType: 'string'},post_date: {bsonType: 'date'},username: {bsonType: 'string'},brief: {bsonType: 'string'},closing_date: {bsonType: 'date'},file_upload: {bsonType: 'object'},title: {bsonType: 'string'},user: {bsonType: 'objectId'},category: {bsonType: 'objectId'}}         }      }});  