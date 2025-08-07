<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-40">
    <div class="flex flex-col items-center gap-2">
        <Rating name="rating" />
        <Message v-if="$form.rating?.invalid" severity="error" size="small" variant="simple">{{ $form.rating.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>