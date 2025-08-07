<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col items-center gap-1">
        <ToggleButton name="consent" class="w-48" onLabel="Accept All" offLabel="Reject All" />
        <Message v-if="$form.consent?.invalid" severity="error" variant="simple">{{ $form.consent.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>