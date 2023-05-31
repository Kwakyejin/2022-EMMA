<script>
  import { Heading, P, A } from "flowbite-svelte";
</script>

<Heading tag="h2" class="mt-5 mb-2">About</Heading>
<Heading tag="h5" class="font-light"
  >Retrosynthesis, READRetro, and the READRetro Website</Heading
>
<Heading tag="h4" class="mt-10 mb-2">Retrosynthesis</Heading>
<P class="mb-3"
  >Retrosynthesis is a problem-solving technique used in organic chemistry to
  design a synthetic route for a target molecule. It involves breaking down the
  target molecule into simpler starting materials, which are then sequentially
  converted into the desired product through a series of chemical reactions. The
  goal of retrosynthesis is to identify the most efficient and practical route
  to synthesize a target molecule. To do this, chemists use a variety of
  strategies and techniques, such as functional group interconversions,
  protecting group chemistry, and stereoselective reactions.</P
>
<P class="mb-3"
  >The retrosynthetic analysis begins with the identification of functional
  groups and other structural features that are likely to be preserved during
  the synthesis. These key functional groups are then used to guide the
  disconnection of the target molecule into smaller fragments. This process is
  repeated until the fragments can be obtained from commercially available
  starting materials or from known synthetic procedures. Once the retrosynthetic
  analysis is complete, the chemist can then plan the forward synthesis by
  selecting appropriate reactions and reagents to connect the fragments in a
  stepwise manner, eventually arriving at the target molecule.</P
>

<Heading tag="h4" class="mt-10 mb-2">READRetro</Heading>
<P class="mb-3"
  >Elucidating the biosynthetic pathways of natural products has been a major
  focus of biochemistry and pharmacy, but predicting the whole pathways from
  target molecules to metabolic building blocks has remained a challenge. Here
  we introduce READRetro, a practical bio-retrosynthesis tool for planning the
  biosynthetic pathways of natural products. READRetro effectively resolved the
  trade-off between generalizability and memorability in bio-retrosynthesis by
  having two separate modules each responsible for each ability.</P
>
<P class="mb-3"
  >Specifically, READRetro utilized a rule-based retriever for memorability and
  an ensemble of two dual representation-based deep learning models for
  generalizability. Through extensive experiments, READRetro was demonstrated to
  outperform existing models by a large margin in both generalizability and
  memorability. READRetro was also capable of predicting the known pathways of
  complex plant secondary metabolites such as monoterpene indole alkaloids,
  demonstrating its applicability to real-world bio-retrosynthesis planning of
  natural products.</P
>

<Heading tag="h4" class="mt-10 mb-2">READRetro Website</Heading>
<P class="mb-3"
  >READRetro was developed as a a web tool designed to assist chemists and
  researchers in tackling the complex problem of retrosynthesis with ease and
  efficiency. The platform is powered by cutting-edge technologies such as
  SvelteKit, FastAPI, Celery, PostgreSQL, and Redis, providing a powerful and
  scalable infrastructure to support your synthetic chemistry endeavors.</P
>
