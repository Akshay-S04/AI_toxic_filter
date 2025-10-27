from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer
from .ai_model import get_toxicity_score

@api_view(['POST'])
def analyze_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        text = serializer.validated_data['text']
        result = get_toxicity_score(text)
        is_toxic = result["score"] > 0.7
        return Response({
            "comment": text,
            "toxicity_label": result["label"],
            "score": result["score"],
            "flagged": is_toxic
        })
    return Response(serializer.errors, status=400)


