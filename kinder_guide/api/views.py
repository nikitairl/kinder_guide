from comments.models import ReviewKindergarten, ReviewSchool
from django.db import transaction
from django.shortcuts import get_object_or_404
from education.models import (Favourites_Kindergartens, Favourites_School,
                              Kindergartens, School, Underground, Area,
                              Language, Profile, AgeCategory, Sport, Create,
                              Intelligence, Music)
from news.models import News
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .permissions import IsAdminOrReadOnly
from .serializers import (AgeCategorySerializer, AreaSerializer,
                          CreateSerializer, IntelligenceSerializer,
                          KindergartensSerializer,
                          KindergartensShortSerializer, LanguageSerializer,
                          MusicSerializer, ProfileSerializer,
                          ReviewKindergartenSerializer, ReviewSchoolSerializer,
                          NewsSerializer, SchoolSerializer,
                          SchoolShortSerializer,
                          UndergroundSerializer, LanguageSerializer,
                          AreaSerializer, SportSerializer, CreateSerializer,
                          MusicSerializer, IntelligenceSerializer,
                          ProfileSerializer, AgeCategorySerializer)


class ReviewKindergartenViewSet(viewsets.ModelViewSet):
    """Вьюсет для Отзывов Десткого сада."""

    queryset = ReviewKindergarten.objects.all()
    serializer_class = ReviewKindergartenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, kindergarten_id):
        kindergarten_id = self.kwargs.get('kindergarten_id')
        queryset = self.queryset.filter(review_post_id=kindergarten_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, kindergarten_id):
        first_name = self.request.user.first_name
        last_name = self.request.user.last_name
        request.data['author'] = f'{first_name} {last_name}'
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(review_post_id=kindergarten_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, kindergarten_id, review_id):
        try:
            review = ReviewKindergarten.objects.get(
                id=review_id,
                review_post_id=kindergarten_id
            )
        except ReviewKindergarten.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, review)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewSchoolViewSet(viewsets.ModelViewSet):
    """Вьюсет для Отзывов школ."""

    queryset = ReviewSchool.objects.all()
    serializer_class = ReviewSchoolSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, school_id):
        school_id = self.kwargs.get('school_id')
        queryset = self.queryset.filter(review_post_id=school_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, school_id):
        request.data['author'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(review_post_id=school_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, school_id, review_id):
        try:
            review = ReviewSchool.objects.get(
                id=review_id,
                review_post_id=school_id
            )
        except ReviewSchool.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, review)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SchoolViewSet(viewsets.ModelViewSet):
    """Вьюсет для Школы."""

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('id', 'name', 'price', 'price_of_year')
    search_fields = ('name', 'description',
                     'telephone', 'address',
                     'email', 'website'
                     )

    def get_serializer_class(self):
        """Переопределение сериализатора для POST запроса."""
        if bool(self.kwargs) is False:
            return SchoolShortSerializer
        return SchoolSerializer

    @transaction.atomic
    @action(detail=True, methods=['POST', 'DELETE'])
    def favorite(self, request, pk=None):
        """Добавляет школу в избранное."""
        user = request.user
        school = get_object_or_404(School, pk=pk)
        if request.method == 'POST':
            favorite, created = Favourites_School.objects.get_or_create(
                user=user,
                school=school
            )
            if created:
                school.is_favorited = True
                school.save()
                return Response(
                    {'detail': 'Школа успешно добавлена в избранное'},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {'detail': 'Школа уже в избранном'},
                    status=status.HTTP_200_OK
                )

        elif request.method == 'DELETE':
            try:
                favorite = Favourites_School.objects.get(
                    user=user,
                    school=school
                )
            except Favourites_School.DoesNotExist:
                return Response(
                    {'detail': 'Школа не в избранном'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            favorite.delete()
            school.is_favorited = False
            school.save()
            return Response(
                {'detail': 'Школа успешно удалена из избранного'},
                status=status.HTTP_204_NO_CONTENT
            )

    @action(detail=False, methods=['get'])
    def all(self, request):
        """Выводит все объекты без пагинации."""
        schools = School.objects.all()
        serializer = SchoolSerializer(
            schools,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class KindergartensViewSet(viewsets.ModelViewSet):
    """Вьюсет для Десткого сада."""

    queryset = Kindergartens.objects.all()
    serializer_class = KindergartensSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('id', 'name', 'price', 'price_of_year')
    search_fields = ('name', 'description',
                     'telephone', 'address',
                     'email', 'website'
                     )

    def get_serializer_class(self):
        """Переопределение сериализатора для POST запроса."""
        if bool(self.kwargs) is False:
            return KindergartensShortSerializer
        return KindergartensSerializer

    @transaction.atomic
    @action(detail=True, methods=['POST', 'DELETE'])
    def favorite(self, request, pk=None):
        """Добавляет детский сад в избранное."""
        user = request.user
        kindergartens = get_object_or_404(Kindergartens, pk=pk)
        if request.method == 'POST':
            favorite, created = Favourites_Kindergartens.objects.get_or_create(
                user=user,
                kindergartens=kindergartens
            )
            if created:
                kindergartens.is_favorited = True
                kindergartens.save()
                return Response(
                    {'detail': 'Детский сад успешно добавлен в избранное'},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {'detail': 'Детский сад уже в избранном'},
                    status=status.HTTP_200_OK
                )

        elif request.method == 'DELETE':
            try:
                favorite = Favourites_Kindergartens.objects.get(
                    user=user,
                    kindergartens=kindergartens
                )
            except Favourites_Kindergartens.DoesNotExist:
                return Response(
                    {'detail': 'Детский сад не в избранном'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            favorite.delete()
            kindergartens.is_favorited = False
            kindergartens.save()
            return Response(
                {'detail': 'Детский сад успешно удален из избранного'},
                status=status.HTTP_204_NO_CONTENT
            )

    @action(detail=False, methods=['get'])
    def all(self, request):
        """Выводит все объекты без пагинации."""
        kindergartens = Kindergartens.objects.all()
        serializer = KindergartensSerializer(
            kindergartens,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class UndergroundViewSet(viewsets.ModelViewSet):
    """Вьюсет для метро."""

    queryset = Underground.objects.all()
    serializer_class = UndergroundSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class AreaViewSet(viewsets.ModelViewSet):
    """Вьюсет для Округа."""

    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class LanguageViewSet(viewsets.ModelViewSet):
    """Вьюсет для Языков."""

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class ProfileViewSet(viewsets.ModelViewSet):
    """Вьюсет для Профилей."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class AgeCategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для Возрастных категорий."""

    queryset = AgeCategory.objects.all()
    serializer_class = AgeCategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class SportViewSet(viewsets.ModelViewSet):
    """Вьюсет для Спортивных занятий."""

    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class CreateViewSet(viewsets.ModelViewSet):
    """Вьюсет для Творческих занятий."""

    queryset = Create.objects.all()
    serializer_class = CreateSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class IntelligenceViewSet(viewsets.ModelViewSet):
    """Вьюсет для Интеллектуальных занятий."""

    queryset = Intelligence.objects.all()
    serializer_class = IntelligenceSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class MusicViewSet(viewsets.ModelViewSet):
    """Вьюсет для Музыкльных занятий."""

    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class FavoriteSchoolViewSet(viewsets.ModelViewSet):
    """Вьюсет для избранного Школы."""

    queryset = School.objects.all()
    serializer_class = SchoolShortSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    http_method_names = ['get']

    def list(self, request):
        user = request.user
        schools = School.objects.filter(favourites_users__user=user)
        serializer = SchoolShortSerializer(
            schools,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class FavoriteKindergartenViewSet(viewsets.ModelViewSet):
    """Вьюсет для избранного Сады."""

    queryset = Kindergartens.objects.all()
    serializer_class = KindergartensShortSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    http_method_names = ['get']

    @action(detail=False, methods=['GET'])
    def favoritekindergartens(self, request):
        kindergartes = self.request.user.favourites_kindergartens
        serializer = KindergartensShortSerializer(kindergartes, many=True)
        return Response(serializer.data)


class NewsViewSet(viewsets.ModelViewSet):
    """Вьюсет для новостей."""

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None

    def list(self, request):
        user = request.user
        kindergartens = Kindergartens.objects.filter(
            favourites_users__user=user
        )
        serializer = KindergartensShortSerializer(
            kindergartens,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
