ユニットテスト名
　・テスト概要
　・入力
　・処理
　・想定出力

ユニットテスト名: CustomUserViewSetTestCase

テスト概要: CustomUserViewSet のテスト
テストメソッド:

test_authenticated_user_can_retrieve_own_user_info
入力: 認証済みのユーザー
処理: 自分自身のユーザー情報を取得
想定出力: ステータスコードが 200 で、ユーザー情報が正しく取得できる

test_unauthenticated_user_cannot_retrieve_user_info
入力: 未認証のユーザー
処理: ユーザー情報を取得しようとする
想定出力: ステータスコードが 403 で、ユーザー情報を取得できない
ユニットテスト名: ProfileViewSetTestCase

テスト概要: ProfileViewSet のテスト
テストメソッド:

test_authenticated_user_can_retrieve_own_profile_info
入力: 認証済みのユーザー
処理: 自分自身のプロフィール情報を取得
想定出力: ステータスコードが 200 で、プロフィール情報が正しく取得できる

test_unauthenticated_user_cannot_retrieve_profile_info
入力: 未認証のユーザー
処理: プロフィール情報を取得しようとする
想定出力: ステータスコードが 403 で、プロフィール情報を取得できない

test_authenticated_user_can_update_own_profile_info
入力: 認証済みのユーザー、更新するプロフィール情報
処理: 自分自身のプロフィール情報を更新
想定出力: ステータスコードが 200 で、プロフィール情報が正しく更新される

test_authenticated_user_can_delete_own_profile_info
入力: 認証済みのユーザー
処理: 自分自身のプロフィール情報を削除
想定出力: ステータスコードが 204 で、プロフィール情報が正しく削除される

test_unauthenticated_user_cannot_update_or_delete_profile_info
入力: 未認証のユーザー、更新するプロフィール情報
処理: プロフィール情報を更新または削除しようとする
想定出力: ステータスコードが 403 で、プロフィール情報を更新または削除できない

ユニットテスト名: CustomUserViewSetTestCase

テスト概要: CustomUserViewSet のテスト
テストメソッド:

3. test_authenticated_user_can_create_custom_user
- 入力: 認証済みのユーザー、新規ユーザー情報
- 処理: 新規ユーザーを作成
- 想定出力: ステータスコードが 201 で、新規ユーザーが正しく作成される
- 
4. test_unauthenticated_user_cannot_create_custom_user
- 入力: 未認証のユーザー、新規ユーザー情報
- 処理: 新規ユーザーを作成しようとする
- 想定出力: ステータスコードが 403 で、新規ユーザーを作成できない
ユニットテスト名: ProfileViewSetTestCase

テスト概要: ProfileViewSet のテスト
テストメソッド:

6. test_authenticated_user_can_create_profile
- 入力: 認証済みのユーザー、新規プロフィール情報
- 処理: 新規プロフィールを作成
- 想定出力: ステータスコードが 201 で、新規プロフィールが正しく作成される
- 
7. test_unauthenticated_user_cannot_create_profile
- 入力: 未認証のユーザー、新規プロフィール情報
- 処理: 新規プロフィールを作成しようとする
- 想定出力: ステータスコードが 403 で、新規プロフィールを作成できない
- 
8. test_authenticated_user_can_list_own_profiles
- 入力: 認証済みのユーザー
- 処理: 自分自身のプロフィール情報を一覧表示
- 想定出力: ステータスコードが 200 で、自分自身のプロフィール情報が正しく一覧表示される
- 
9. test_unauthenticated_user_cannot_list_profiles
- 入力: 未認証のユーザー
- 処理: プロフィール情報を一覧表示しようとする
- 想定出力: ステータスコードが 403 で、プロフィール情報を一覧表示できない

ユニットテスト名: CustomUserViewSetTestCase

テスト概要: CustomUserViewSet のテスト
テストメソッド:

5. test_authenticated_user_can_update_own_custom_user
- 入力: 認証済みのユーザー、更新したいユーザー情報
- 処理: 自分自身のユーザー情報を更新
- 想定出力: ステータスコードが 200 で、ユーザー情報が正しく更新される
- 
6. test_unauthenticated_user_cannot_update_custom_user
- 入力: 未認証のユーザー、更新したいユーザー情報
- 処理: ユーザー情報を更新しようとする
- 想定出力: ステータスコードが 403 で、ユーザー情報を更新できない
ユニットテスト名: ProfileViewSetTestCase

テスト概要: ProfileViewSet のテスト
テストメソッド:

10. test_authenticated_user_can_update_own_profile
- 入力: 認証済みのユーザー、更新したいプロフィール情報
- 処理: 自分自身のプロフィール情報を更新
- 想定出力: ステータスコードが 200 で、プロフィール情報が正しく更新される
- 
11. test_unauthenticated_user_cannot_update_profile
- 入力: 未認証のユーザー、更新したいプロフィール情報
- 処理: プロフィール情報を更新しようとする
- 想定出力: ステータスコードが 403 で、プロフィール情報を更新できない
- 
12. test_authenticated_user_can_delete_own_profile
- 入力: 認証済みのユーザー
- 処理: 自分自身のプロフィール情報を削除
- 想定出力: ステータスコードが 204 で、プロフィール情報が正しく削除される
- 
13. test_unauthenticated_user_cannot_delete_profile
- 入力: 未認証のユーザー
- 処理: プロフィール情報を削除しようとする
- 想定出力: ステータスコードが 403 で、プロフィール情報を削除できない

ユニットテスト名: CustomUserViewSetTestCase

テスト概要: CustomUserViewSet のテスト
テストメソッド:
7. test_authenticated_user_can_delete_own_custom_user
- 入力: 認証済みのユーザー
- 処理: 自分自身のユーザー情報を削除
- 想定出力: ステータスコードが 204 で、ユーザー情報が正しく削除される
8. test_unauthenticated_user_cannot_delete_custom_user
- 入力: 未認証のユーザー
- 処理: ユーザー情報を削除しようとする
- 想定出力: ステータスコードが 403 で、ユーザー情報を削除できない
ユニットテスト名: ProfileViewSetTestCase

テスト概要: ProfileViewSet のテスト
テストメソッド:

14. test_authenticated_user_can_create_profile
- 入力: 認証済みのユーザー、新しいプロフィール情報
- 処理: 新しいプロフィール情報を作成
- 想定出力: ステータスコードが 201 で、新しいプロフィール情報が正しく作成される
- 
15. test_unauthenticated_user_cannot_create_profile
- 入力: 未認証のユーザー、新しいプロフィール情報
- 処理: 新しいプロフィール情報を作成しようとする
- 想定出力: ステータスコードが 403 で、新しいプロフィール情報を作成できない
- 
16. test_authenticated_user_can_list_profiles
- 入力: 認証済みのユーザー
- 処理: プロフィール情報の一覧を取得
- 想定出力: ステータスコードが 200 で、プロフィール情報の一覧が正しく取得できる
- 
17. test_unauthenticated_user_cannot_list_profiles
- 入力: 未認証のユーザー
- 処理: プロフィール情報の一覧を取得しようとする
- 想定出力: ステータスコードが 403 で、プロフィール情報の一覧が取得できない

ユニットテスト名: ProfileViewSetTestCase

テスト概要: ProfileViewSet のテスト
テストメソッド:

18. test_authenticated_user_can_retrieve_own_profile
- 入力: 認証済みのユーザー
- 処理: 自分自身のプロフィール情報を取得
- 想定出力: ステータスコードが 200 で、自分自身のプロフィール情報が正しく取得できる
- 
19. test_unauthenticated_user_cannot_retrieve_profile
- 入力: 未認証のユーザー
- 処理: プロフィール情報を取得しようとする
- 想定出力: ステータスコードが 403 で、プロフィール情報が取得できない
- 
20. test_authenticated_user_can_update_own_profile
- 入力: 認証済みのユーザー、変更後のプロフィール情報
- 処理: 自分自身のプロフィール情報を更新
- 想定出力: ステータスコードが 200 で、自分自身のプロフィール情報が正しく更新される
- 
21. test_unauthenticated_user_cannot_update_profile
- 入力: 未認証のユーザー、変更後のプロフィール情報
- 処理: プロフィール情報を更新しようとする
- 想定出力: ステータスコードが 403 で、プロフィール情報を更新できない
- 
22. test_authenticated_user_can_delete_own_profile
- 入力: 認証済みのユーザー
- 処理: 自分自身のプロフィール情報を削除
- 想定出力: ステータスコードが 204 で、自分自身のプロフィール情報が正しく削除される
- 
23. test_unauthenticated_user_cannot_delete_profile
- 入力: 未認証のユーザー
- 処理: プロフィール情報を削除しようとする
- 想定出力: ステータスコードが 403 で、プロフィール情報を削除できない
- 