from rest_framework import serializers

from animals.models import Animal
from characteristics.models import Characteristic
from groups.models import Group

from characteristics.serializers import CharacteristicSerializer
from groups.serializers import GroupSerializer

# Create your models here.

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()

    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)
    
    def create(self, validated_data):
        group = validated_data.pop("group")
        characteristics = validated_data.pop("characteristics")

        create_group = Group.objects.create(**group)
        create_animal = Animal.objects.create(**validated_data, group=create_group)
        
        for characteristic in characteristics:
            create_characteristic = Characteristic.objects.create(**characteristic)
            create_animal.characteristics.add(create_characteristic)

        return create_animal


    def update(self, instance, validated_data):
        no_update_keys = ["sex", "group"]
        wrong_keys = []

        for key, value in validated_data.items():
            if(key in no_update_keys):
                wrong_keys.append(key)

        if(wrong_keys):
            raise KeyError ({
                "message": f"You can not update {wrong_keys} property."
            })

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance