+-------------------+     +----------------+     +--------------------+
|   CustomUser      |     |   Profile      |     |   Post             |
+-------------------+     +----------------+     +--------------------+
| - id              |1---1| - custom_user  |1---*| - author           |
| - username        |     | - display_name |     | - title            |
| - email           |     | - bio          |     | - content          |
| - first_name      |     +----------------+     | - created_at       |
| - last_name       |                              | - updated_at       |
+-------------------+                              +--------------------+
|                   |                              |                    |
|   sns_app models  |                              |   sns_app models   |
+-------------------+                              +--------------------+


+-------------------+     +----------------+     +--------------------+      +---------+     +--------------+
|   CustomUser      |     |   Profile      |     |   Post             |      |  Like   |     |  Comment     |
+-------------------+     +----------------+     +--------------------+      +---------+     +--------------+
| - id              |1---1| - custom_user  |1---*| - custom_user      |      | - id    |     | - id         |
| - username        |     | - display_name |     | - content          |*----1| - custom_user|1---*| - custom_user|
| - email           |     | - bio          |     | - created_at       |      | - post  |     | - post       |
| - first_name      |     +----------------+     +--------------------+      +---------+     | - content    |
| - last_name       |                                                                  |     | - created_at |
+-------------------+                                                                  |     | - updated_at |
|                   |                                                                  |     +--------------+
|   sns_app models  |                                                                  |
+-------------------+                                                                  |
                                                                                        |
+-------------------+                                                                  |
|   CustomUser      |                                                                  |
| (as Follower)     |                                                                  |
| - id              |                                                                  |
+-------------------+                                                                  |
|                   |     +---------------+                                           |
|   sns_app models  |1---*|   Follow      |*---1                                      |
+-------------------+     +---------------+     +-------------------+                 |
                          | - follower    |     |   CustomUser      |                 |
                          | - followed    |     | (as Followed)     |                 |
                          | - timestamp   |     | - id              |                 |
                          +---------------+     +-------------------+                 |
                                                |                   |                 |
                                                |   sns_app models  |                 |
                                                +-------------------+                 |

