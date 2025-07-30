from datetime import date, timedelta

from rest_framework import serializers

from manage_subscription.models import Plan, Subscription


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)
    plan_id = serializers.PrimaryKeyRelatedField(
        queryset=Plan.objects.filter(), write_only=True
    )

    class Meta:
        model = Subscription
        fields = ["plan", "plan_id", "start_date", "end_date", "status"]
        read_only_fields = ["plan", "start_date", "end_date", "status"]

    def create(self, validated_data):
        plan = validated_data.pop("plan_id")
        user = self.context.get("request").user
        start_date = date.today()
        end_date = start_date + timedelta(days=plan.duration_days)
        validated_data["user_id"] = user.id
        validated_data["plan_id"] = plan.id
        validated_data["start_date"] = start_date
        validated_data["end_date"] = end_date
        return Subscription.objects.create(**validated_data)


class SubscriptionCancelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["status"]
