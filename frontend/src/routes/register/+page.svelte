<script>
  import {
    Button,
    Modal,
    Label,
    Input,
    Checkbox,
    Heading,
  } from "flowbite-svelte";
  import { Textarea } from "flowbite-svelte";

  let name;
  let Introduction;

  async function fetch_register() {
    try {
      const response = await fetch(
        `http://10.125.218.100:9025/upload?input_a=${name}&input_b=${Introduction}`,
        {
          mode: "cors",
        }
      );

      if (response.ok) {
        const result = await response.json();
        console.log(result);
        document.location.href = `/emma/${id}`;
      } else {
        console.error("Error:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }
</script>

<div class="h-full w-full p-52">
  <form class="flex flex-col space-y-6" action="#">
    <Heading tag="h2" class="mt-5 mb-2">Create Account</Heading>
    <Label for="name" class="space-y-2">
      <span>Your name</span>
      <Input
        type="text"
        id="name"
        bind:value={name}
        placeholder="Kwak Ye Jin"
        required
      />
    </Label>

    <Label for="textarea-id" class="space-y-2">
      <span>Your Introduction</span>
      <Textarea
        id="textarea-id"
        placeholder="Your Introduction"
        bind:value={Introduction}
        rows="4"
        name="Introduction"
      />
    </Label>
    <div class="flex items-start">
      <Button on:click={() => fetch_register()} type="submit" class="w-full"
        >Create My EMMA</Button
      >
    </div>
  </form>
</div>
