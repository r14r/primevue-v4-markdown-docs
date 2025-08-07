<Toast position="bottom-center" group="bc" @close="onClose">
    <template #message="slotProps">
        <div class="flex flex-col items-start flex-auto">
            <div class="flex items-center gap-2">
                <Avatar image="https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png" shape="circle" />
                <span class="font-bold">Amy Elsner</span>
            </div>
            <div class="font-medium text-lg my-4">{{ slotProps.message.summary }}</div>
            <Button size="small" label="Reply" severity="success" @click="onReply()"></Button>
        </div>
    </template>
</Toast>
<Button @click="showTemplate" label="View" />