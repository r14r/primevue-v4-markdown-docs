<Button label="Show" @click="addMessages()" />
<Button label="Clear" severity="secondary" class="ml-2" @click="clearMessages()" />
<transition-group name="p-message" tag="div" class="flex flex-col">
    <Message v-for="msg of messages" :key="msg.id" :severity="msg.severity" class="mt-4">{{ msg.content }}</Message>
</transition-group>