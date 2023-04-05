| API エンドポイント      | HTTP メソッド | 機能                     |
|--------------------|------------|------------------------|
| /api/token/        | POST        | トークンベースの認証               | いいえ      |
| /api/token/refresh/ | POST        | アクセストークンの更新             | はい        |
| /api/token/revoke/ | POST        | アクセストークンの無効化           | はい        |

| API エンドポイント | HTTP メソッド | 機能                          | 認証が必要 |
|-------------|-------------|-----------------------------|-----------|
| /api/custom_users/ | POST        | 新規ユーザー登録                  | いいえ      |
| /api/custom_users/ | GET         | ユーザー一覧の取得                | はい        |
| /api/custom_users/{id}/ | GET      | 指定ユーザーの取得                | はい        |
| /api/custom_users/{id}/ | PUT      | 指定ユーザーの更新                | はい        |
| /api/custom_users/{id}/ | DELETE   | 指定ユーザーの削除                | はい        |
|||
| /api/posts/ | POST        | 新規投稿の作成                   | はい        |
| /api/posts/ | GET         | 投稿一覧の取得                   | はい        |
| /api/posts/{id}/ | GET         | 指定投稿の取得                   | はい        |
| /api/posts/{id}/ | PUT         | 指定投稿の更新                   | はい        |
| /api/posts/{id}/ | DELETE      | 指定投稿の削除                   | はい        |
|||
| /api/likes/ | POST        | 新規いいねの作成                 | はい        |
| /api/likes/ | GET         | いいね一覧の取得                 | はい        |
| /api/likes/{id}/ | DELETE      | 指定いいねの削除                 | はい        |
|||
| /api/comments/ | POST        | 新規コメントの作成                | はい        |
| /api/comments/ | GET         | コメント一覧の取得                | はい        |
| /api/comments/{id}/ | GET         | 指定コメントの取得                | はい        |
| /api/comments/{id}/ | PUT         | 指定コメントの更新                | はい        |
| /api/comments/{id}/ | DELETE      | 指定コメントの削除                | はい        |
|             |           |                             |       |
| /api/follows/ | POST        | 新規フォローの作成                | はい        |
| /api/follows/ | GET         | フォロー一覧の取得                | はい        |
| /api/follows/{id}/ | DELETE      | 指定フォローの削除                | はい        |
|||
| /api/profiles/{id}/ | GET         | 指定プロフィールの取得             | はい        |
| /api/profiles/{id}/ | PUT         | 指定プロフィールの更新             | はい        |
| /api/profiles/{id}/ | DELETE      | 指定プロフィールの削除             | はい        |


