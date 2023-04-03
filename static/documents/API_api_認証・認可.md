| API エンドポイント      | HTTP メソッド | 機能                     |
|-----------------------|------------|------------------------|
| /api/v1/token/         | POST        | トークンベースの認証               | いいえ      |
| /api/v1/token/refresh/ | POST        | アクセストークンの更新             | はい        |
| /api/v1/token/revoke/  | POST        | アクセストークンの無効化           | はい        |

| API エンドポイント        | HTTP メソッド | 機能                          | 認証が必要 |
|------------------------|-------------|-----------------------------|-----------|
| /api/v1/custom_users/  | POST        | 新規ユーザー登録                  | いいえ      |
| /api/v1/custom_users/  | GET         | ユーザー一覧の取得                | はい        |
| /api/v1/custom_users/{id}/ | GET      | 指定ユーザーの取得                | はい        |
| /api/v1/custom_users/{id}/ | PUT      | 指定ユーザーの更新                | はい        |
| /api/v1/custom_users/{id}/ | DELETE   | 指定ユーザーの削除                | はい        |
|||
| /api/v1/posts/          | POST        | 新規投稿の作成                   | はい        |
| /api/v1/posts/          | GET         | 投稿一覧の取得                   | はい        |
| /api/v1/posts/{id}/     | GET         | 指定投稿の取得                   | はい        |
| /api/v1/posts/{id}/     | PUT         | 指定投稿の更新                   | はい        |
| /api/v1/posts/{id}/     | DELETE      | 指定投稿の削除                   | はい        |
|||
| /api/v1/likes/          | POST        | 新規いいねの作成                 | はい        |
| /api/v1/likes/          | GET         | いいね一覧の取得                 | はい        |
| /api/v1/likes/{id}/     | DELETE      | 指定いいねの削除                 | はい        |
|||
| /api/v1/comments/       | POST        | 新規コメントの作成                | はい        |
| /api/v1/comments/       | GET         | コメント一覧の取得                | はい        |
| /api/v1/comments/{id}/  | GET         | 指定コメントの取得                | はい        |
| /api/v1/comments/{id}/  | PUT         | 指定コメントの更新                | はい        |
| /api/v1/comments/{id}/  | DELETE      | 指定コメントの削除                | はい        |
|                    |           |                             |       |
| /api/v1/follows/        | POST        | 新規フォローの作成                | はい        |
| /api/v1/follows/        | GET         | フォロー一覧の取得                | はい        |
| /api/v1/follows/{id}/   | DELETE      | 指定フォローの削除                | はい        |
|||
| /api/v1/profiles/{id}/  | GET         | 指定プロフィールの取得             | はい        |
| /api/v1/profiles/{id}/  | PUT         | 指定プロフィールの更新             | はい        |
| /api/v1/profiles/{id}/  | DELETE      | 指定プロフィールの削除             | はい        |


