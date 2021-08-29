import graphene
from graphene_django import DjangoObjectType
from .models import FieldWorker


class FieldWorkerGraphQL(DjangoObjectType):
    class Meta:
        model = FieldWorker
        fields = '__all__'


class Query(graphene.ObjectType):
    fieldworkers = graphene.List(FieldWorkerGraphQL)

    def resolve_fieldworkers(root, info, **kwargs):
        return FieldWorker.objects.all()


class FieldWorkerInput(graphene.InputObjectType):
    firstName = graphene.String()
    lastName = graphene.String()
    function = graphene.String()


class CreateFieldWorker(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        input = FieldWorkerInput(required=True)

    # Class attributes define the response of the mutation
    fieldwork = graphene.Field(FieldWorkerGraphQL)

    @classmethod
    def mutate(cls, root, info, input):
        fieldwork = FieldWorker()
        fieldwork.first_name = input.firstName
        fieldwork.last_name = input.lastName
        fieldwork.function = input.function
        fieldwork.save()
        return CreateFieldWorker(fieldwork=fieldwork)


class UpdateFieldWorker(graphene.Mutation):
    class Arguments:
        input = FieldWorkerInput(required=False)
        id = graphene.ID()

    fieldwork = graphene.Field(FieldWorkerGraphQL)

    @classmethod
    def mutate(cls, root, info, input, id):
        fieldwork = FieldWorker.objects.get(pk=id)
        if input.firstName:
            fieldwork.first_name = input.firstName
        if input.lastName:
            fieldwork.last_name = input.lastName
        if input.function:
            fieldwork.function = input.function
        fieldwork.save()
        return UpdateFieldWorker(fieldwork=fieldwork)


class DeleteFieldWorker(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    fieldwork = graphene.Field(FieldWorkerGraphQL)

    @classmethod
    def mutate(cls, root, info, id):
        fieldwork = FieldWorker.objects.get(pk=id)
        fieldwork.delete()
        return DeleteFieldWorker(fieldwork=fieldwork)


class Mutation(graphene.ObjectType):
    create_field_worker = CreateFieldWorker.Field()
    update_field_worker = UpdateFieldWorker.Field()
    delete_field_worker = DeleteFieldWorker.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)