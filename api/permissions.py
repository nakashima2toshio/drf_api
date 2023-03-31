from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    オブジェクトの所有者だけが編集できるようにするカスタムパーミッション。
    それ以外のユーザーは読み取り専用です。
    """

    def has_object_permission(self, request, view, obj):
        # 読み取り専用のパーミッションは、すべてのリクエストに対して許可されます。
        if request.method in permissions.SAFE_METHODS:
            return True

        # オブジェクトの所有者だけが編集できるようにします。
        return obj.owner == request.user

"""
この例では、IsOwnerOrReadOnlyというカスタムパーミッションクラスを作成しています。
このクラスは、オブジェクトの所有者だけが編集できるように制限します。
それ以外のユーザーは、読み取り専用のアクセスしかできません。
このカスタムパーミッションをビューに適用するには、permission_classes属性に追加します。
"""

"""
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer
from .permissions import IsOwnerOrReadOnly

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
"""