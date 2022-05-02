from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import User, Hall, Category, Food, Service, \
    User, Order, Feedback, Customer, Regulation, Menu
from rest_framework import viewsets, generics, status, permissions
from .serializers import CustomerSerializer, HallSerializer, CategorySerializer, \
    OrderSerializer, ServiceSerializer, FeedbackSerializer, FoodSerializer, \
    MenuSerializer
from .paginators import BasePaginator
from .change_price_halls import *


class CustomerViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer

    @action(methods=['post'], detail=True, url_path='add-add-cus')
    def add_in_cus(self, request, pk):
        user = self.get_object()
        customer = Customer.objects.create(phone_number="13214", user=user)
        customer.save()


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        query = self.queryset

        kw = self.request.query_params.get('kw')
        if kw:
            query = query.filter(name__icontains=kw)

        return query

    @action(methods=['get'], detail=True, url_path='foods')
    def get_lessons(self, request, pk):
        category = Category.objects.get(pk=pk)
        foods = category.foods.filter(active=True)

        kw = request.query_params.get('kw')
        if kw is not None:
            foods = foods.filter(name__icontains=kw)

        price = request.query_params.get('price')
        if price is not None:
            foods = foods.filter(price=price)

        return Response(data=FoodSerializer(foods, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class HallViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Hall.objects.filter(active=True)
    serializer_class = HallSerializer
    pagination_class = BasePaginator
    price_hall_now()

    def get_queryset(self):
        query = self.queryset

        kw = self.request.query_params.get('kw')
        if kw:
            query = query.filter(name__icontains=kw)
            return query

        qty = self.request.query_params.get('qty')
        if qty:
            query = query.filter(capacity=qty)
            return query

        return query


# class FoodViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
#     queryset = Food.objects.filter(active=True)
#     serializer_class = FoodSerializer
#     pagination_class = BasePaginator
#
#     def get_queryset(self):
#         query = self.queryset
#
#         kw = self.request.query_params.get('kw')
#         if kw:
#             query = query.filter(name__icontains=kw)
#             return query
#
#         price = self.request.query_params.get('price')
#         if price:
#             query = query.filter(price=price)
#             return query
#
#         return query


class ServiceViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Service.objects.filter(active=True)
    serializer_class = ServiceSerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        query = self.queryset

        kw = self.request.query_params.get('kw')
        if kw:
            query = query.filter(name__icontains=kw)
            return query

        price = self.request.query_params.get('price')
        if price:
            query = query.filter(price=price)
            return query

        return query


class MenuViewSet(viewsets.ViewSet, generics. ListAPIView, generics.RetrieveAPIView):
    queryset = Menu.objects.filter(active=True)
    serializer_class = MenuSerializer


class OrderViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post'], detail=True, url_path='time_organize')
    def choose_time_organize(self, request, pk):
        order = Order.objects.get(pk=pk)
        date = request.data.get('date')
        shift = int(request.data.get('shift'))

        if date and shift is not None:
            time_organize, _ = DateOfOrganization.objects.get_or_create(date=date, shift=shift)
            order.time_organize = time_organize
            order.save()

        return Response(self.serializer_class(order).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='choose-menu')
    def choose_menu(self, request, pk):
        order = Order.objects.get(pk=pk)
        m = request.data.get('menu')
        menu = Menu.objects.get(pk=m)

        if menu is not None:
            order.menu = menu
            order.save()
        return Response(self.serializer_class(order).data, status=status.HTTP_200_OK)

    # @action(methods=['post'], detail=True, url_path='feedbacks')
    # def get_feedbacks(self, request, pk):
    #     content =request.data.get('content')
    #     if content:
    #         c = Feedback.objects.create(content=content, wedding=self.get_object(), crea

    # return Response(FeedbackSerializer(feedbacks, many=True).data, status=status.HTTP_200_OK)


class FeedbackViewSet(viewsets.ViewSet, generics.CreateAPIView,
                      generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Feedback.objects.filter(active=True)
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]
