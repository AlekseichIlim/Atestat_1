from rest_framework import serializers

from sales_network.models import NetworkLink


class NetworkLinkSerializer(serializers.ModelSerializer):
    url_provider = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = NetworkLink
        fields = "__all__"


    def get_url_provider(self, obj):
        if obj.provider is not None:
            return obj.provider.email


class NetworkLinkWithoutArrearsField(serializers.ModelSerializer):
    """Сериализатор без поля задолжности перед поставщиком """

    url_provider = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = NetworkLink
        exclude = ('arrears', )

    def get_url_provider(self, obj):
        if obj.provider is not None:
            return obj.provider.email

# class SubscriptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subscription
#         fields = '__all__'
#
#
# class CourseSerializer(serializers.ModelSerializer):
#     count_lessons = serializers.SerializerMethodField(read_only=True)
#     lesson = LessonSerializer(many=True, read_only=True)
#     subscription = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = Course
#         fields = "__all__"
#
#     #         поля которые будут в ответе Postman
#
#     def get_count_lessons(self, instance):
#
#         return instance.lesson.all().count()
#
#     def get_subscription(self, obj):
#         user = self.context['request'].user
#         if Subscription.objects.filter(user=user, course=obj).exists():
#             return "Оформлена подписка"
#         return "Не оформлена подписка"
